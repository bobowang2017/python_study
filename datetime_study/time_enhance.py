# -*- coding: utf-8 -*-
import unittest
from datetime import datetime, date

import arrow


class TimeArrow(unittest.TestCase):
    def setUp(self) -> None:
        self.current_time = arrow.now()

    def test_compute_time(self):
        print(self.current_time)
        old_time = self.current_time.shift(months=-1)
        print(old_time)

    def test_humanize(self):
        print(self.current_time.humanize(locale="zh"))
        old_time = self.current_time.shift(months=-1)
        print(old_time.humanize(locale="zh"))

    def test_format(self):
        print(self.current_time.format("YYYY-MM-DD HH:mm:ss"))

    def test_time_calculate(self):
        old_time = arrow.get(datetime(2018, 8, 24))
        print(old_time.humanize(locale='zh'))

    def test_get_instance(self):
        print(arrow.get())
        print(arrow.get(datetime(2019, 10, 25)).humanize(locale="zh"))
        print(arrow.get(date(2018, 7, 24)))
        print(arrow.get("2018-08-11 12:30:56"))
        print(arrow.get("18-08-11 12:30:56", "YY-MM-DD HH:mm:ss"))

