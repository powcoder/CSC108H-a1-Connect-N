https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# Copyright (c) 2016, 2018 Claudiu Popa <pcmanticore@gmail.com>
# Copyright (c) 2018 Bryce Guinta <bryce.paul.guinta@gmail.com>

"""Astroid hooks for understanding functools library module."""
from itertools import chain

import astroid
from astroid import arguments
from astroid import BoundMethod
from astroid import extract_node
from astroid import helpers
from astroid.interpreter import objectmodel
from astroid import MANAGER


LRU_CACHE = 'functools.lru_cache'


class LruWrappedModel(objectmodel.FunctionModel):
    """Special attribute model for functions decorated with functools.lru_cache.

    The said decorators patches at decoration time some functions onto
    the decorated function.
    """

    @property
    def py__wrapped__(self):
        return self._instance

    @property
    def pycache_info(self):
        cache_info = extract_node('''
        from functools import _CacheInfo
        _CacheInfo(0, 0, 0, 0)
        ''')
        class CacheInfoBoundMethod(BoundMethod):
            def infer_call_result(self, caller, context=None):
                yield helpers.safe_infer(cache_info)

        return CacheInfoBoundMethod(proxy=self._instance, bound=self._instance)

    @property
    def pycache_clear(self):
        node = extract_node('''def cache_clear(self): pass''')
        return BoundMethod(proxy=node, bound=self._instance.parent.scope())


def _transform_lru_cache(node, context=None):
    # TODO: this is not ideal, since the node should be immutable,
    # but due to https://github.com/PyCQA/astroid/issues/354,
    # there's not much we can do now.
    # Replacing the node would work partially, because,
    # in pylint, the old node would still be available, leading
    # to spurious false positives.
    node.special_attributes = LruWrappedModel()(node)
    return


def _functools_partial_inference(node, context=None):
    call = arguments.CallSite.from_call(node)
    number_of_positional = len(call.positional_arguments)
    if number_of_positional < 1:
        raise astroid.UseInferenceDefault('functools.partial takes at least one argument')
    if number_of_positional == 1 and not call.keyword_arguments:
        raise astroid.UseInferenceDefault(
            'functools.partial needs at least to have some filled arguments'
        )

    partial_function = call.positional_arguments[0]
    try:
        inferred_wrapped_function = next(partial_function.infer(context=context))
    except astroid.InferenceError as exc:
        raise astroid.UseInferenceDefault from exc
    if inferred_wrapped_function is astroid.Uninferable:
        raise astroid.UseInferenceDefault('Cannot infer the wrapped function')
    if not isinstance(inferred_wrapped_function, astroid.FunctionDef):
        raise astroid.UseInferenceDefault('The wrapped function is not a function')

    # Determine if the passed keywords into the callsite are supported
    # by the wrapped function.
    function_parameters = chain(
        inferred_wrapped_function.args.args or (),
        inferred_wrapped_function.args.kwonlyargs or ()
    )
    parameter_names = set(
        param.name for param in function_parameters
        if isinstance(param, astroid.AssignName)
    )
    if set(call.keyword_arguments) - parameter_names:
        raise astroid.UseInferenceDefault('wrapped function received unknown parameters')

    # Return a wrapped() object that can be used further for inference
    class PartialFunction(astroid.FunctionDef):

        filled_positionals = len(call.positional_arguments[1:])
        filled_keywords = list(call.keyword_arguments)

        def infer_call_result(self, caller=None, context=None):
            nonlocal call
            filled_args = call.positional_arguments[1:]
            filled_keywords = call.keyword_arguments

            if context:
                current_passed_keywords = {
                    keyword for (keyword, _) in context.callcontext.keywords
                }
                for keyword, value in filled_keywords.items():
                    if keyword not in current_passed_keywords:
                        context.callcontext.keywords.append((keyword, value))

                call_context_args = context.callcontext.args or []
                context.callcontext.args = filled_args + call_context_args

            return super().infer_call_result(
                caller=caller,
                context=context,
            )

    partial_function = PartialFunction(
        name=inferred_wrapped_function.name,
        doc=inferred_wrapped_function.doc,
        lineno=inferred_wrapped_function.lineno,
        col_offset=inferred_wrapped_function.col_offset,
        parent=inferred_wrapped_function.parent,
    )
    partial_function.postinit(
        args=inferred_wrapped_function.args,
        body=inferred_wrapped_function.body,
        decorators=inferred_wrapped_function.decorators,
        returns=inferred_wrapped_function.returns,
        type_comment_returns=inferred_wrapped_function.type_comment_returns,
        type_comment_args=inferred_wrapped_function.type_comment_args,
    )
    return iter((partial_function,))


def _looks_like_lru_cache(node):
    """Check if the given function node is decorated with lru_cache."""
    if not node.decorators:
        return False

    for decorator in node.decorators.nodes:
        if not isinstance(decorator, astroid.Call):
            continue

        func = helpers.safe_infer(decorator.func)
        if func in (None, astroid.Uninferable):
            continue

        if isinstance(func, astroid.FunctionDef) and func.qname() == LRU_CACHE:
            return True
    return False


def _looks_like_functools_partial(node):
    """Check if the given Call node is a functools.partial call"""
    if isinstance(node.func, astroid.Name):
        return node.func.name == 'partial'
    elif isinstance(node.func, astroid.Attribute):
        return (node.func.attrname == 'partial'
                and isinstance(node.func.expr, astroid.Name)
                and node.func.expr.name == 'functools')


MANAGER.register_transform(
    astroid.FunctionDef,
    _transform_lru_cache,
    _looks_like_lru_cache,
)


MANAGER.register_transform(
    astroid.Call,
    astroid.inference_tip(_functools_partial_inference),
    _looks_like_functools_partial,
)
