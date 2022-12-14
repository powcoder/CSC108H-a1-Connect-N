https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2018 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import


class HypothesisException(Exception):
    """Generic parent class for exceptions thrown by Hypothesis."""


class CleanupFailed(HypothesisException):
    """At least one cleanup task failed and no other exception was raised."""


class UnsatisfiedAssumption(HypothesisException):
    """An internal error raised by assume.

    If you're seeing this error something has gone wrong.
    """


class BadTemplateDraw(HypothesisException):
    """An internal error raised when something unfortunate happened during
    template generation and you should restart the draw, preferably with a new
    parameter.

    This is not an error condition internally, but if you ever see this
    in your code it's probably a Hypothesis bug
    """


class NoSuchExample(HypothesisException):
    """The condition we have been asked to satisfy appears to be always false.

    This does not guarantee that no example exists, only that we were
    unable to find one.
    """

    def __init__(self, condition_string, extra=''):
        super(NoSuchExample, self).__init__(
            'No examples found of condition %s%s' % (
                condition_string, extra)
        )


class DefinitelyNoSuchExample(NoSuchExample):  # pragma: no cover
    """Hypothesis used to be able to detect exhaustive coverage of a search
    space and no longer can.

    This exception remains for compatibility reasons for now but can
    never actually be thrown.
    """


class NoExamples(HypothesisException):
    """Raised when example() is called on a strategy but we cannot find any
    examples after enough tries that we really should have been able to if this
    was ever going to work."""


class Unsatisfiable(HypothesisException):
    """We ran out of time or examples before we could find enough examples
    which satisfy the assumptions of this hypothesis.

    This could be because the function is too slow. If so, try upping
    the timeout. It could also be because the function is using assume
    in a way that is too hard to satisfy. If so, try writing a custom
    strategy or using a better starting point (e.g if you are requiring
    a list has unique values you could instead filter out all duplicate
    values from the list)
    """


class Flaky(HypothesisException):
    """This function appears to fail non-deterministically: We have seen it
    fail when passed this example at least once, but a subsequent invocation
    did not fail.

    Common causes for this problem are:
        1. The function depends on external state. e.g. it uses an external
           random number generator. Try to make a version that passes all the
           relevant state in from Hypothesis.
        2. The function is suffering from too much recursion and its failure
           depends sensitively on where it's been called from.
        3. The function is timing sensitive and can fail or pass depending on
           how long it takes. Try breaking it up into smaller functions which
           don't do that and testing those instead.
    """


class Timeout(Unsatisfiable):
    """We were unable to find enough examples that satisfied the preconditions
    of this hypothesis in the amount of time allotted to us."""


class WrongFormat(HypothesisException, ValueError):
    """An exception indicating you have attempted to serialize a value that
    does not match the type described by this format."""


class BadData(HypothesisException, ValueError):
    """The data that we got out of the database does not seem to match the data
    we could have put into the database given this schema."""


class InvalidArgument(HypothesisException, TypeError):
    """Used to indicate that the arguments to a Hypothesis function were in
    some manner incorrect."""


class ResolutionFailed(InvalidArgument):
    """Hypothesis had to resolve a type to a strategy, but this failed.

    Type inference is best-effort, so this only happens when an
    annotation exists but could not be resolved for a required argument
    to the target of ``builds()``, or where the user passed ``infer``.
    """


class InvalidState(HypothesisException):
    """The system is not in a state where you were allowed to do that."""


class InvalidDefinition(HypothesisException, TypeError):
    """Used to indicate that a class definition was not well put together and
    has something wrong with it."""


class AbnormalExit(HypothesisException):
    """Raised when a test running in a child process exits without returning or
    raising an exception."""


class FailedHealthCheck(HypothesisException, Warning):
    """Raised when a test fails a preliminary healthcheck that occurs before
    execution."""

    def __init__(self, message, check):
        super(FailedHealthCheck, self).__init__(message)
        self.health_check = check


class HypothesisWarning(HypothesisException, Warning):
    """A generic warning issued by Hypothesis."""


class HypothesisDeprecationWarning(HypothesisWarning, FutureWarning):
    """A deprecation warning issued by Hypothesis.

    Actually inherits from FutureWarning, because DeprecationWarning is
    hidden by the default warnings filter.
    """


class Frozen(HypothesisException):
    """Raised when a mutation method has been called on a ConjectureData object
    after freeze() has been called."""


class MultipleFailures(HypothesisException):
    """Indicates that Hypothesis found more than one distinct bug when testing
    your code."""


class DeadlineExceeded(HypothesisException):
    """Raised when an individual test body has taken too long to run."""

    def __init__(self, runtime, deadline):
        super(DeadlineExceeded, self).__init__((
            'Test took %.2fms, which exceeds the deadline of '
            '%.2fms') % (runtime, deadline))
        self.runtime = runtime
        self.deadline = deadline


class StopTest(BaseException):

    def __init__(self, testcounter):
        super(StopTest, self).__init__(repr(testcounter))
        self.testcounter = testcounter


class DidNotReproduce(HypothesisException):
    pass
