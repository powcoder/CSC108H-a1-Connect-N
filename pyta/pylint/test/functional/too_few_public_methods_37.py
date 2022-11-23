https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# pylint: disable=missing-docstring
import dataclasses
from dataclasses import dataclass


@dataclasses.dataclass
class ScheduledTxSearchModel:
    date_from = None
    date_to = None


@dataclass
class ScheduledTxSearchModelOne:
    date = None
