# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from forgery_py.forgery import basic


class BasicForgeryTestCase(TestCase):
    def test_hex_color(self):
        color = basic.hex_color()

        assert re.match(r'[0-9A-F]{6}$', color) is not None

    def test_hex_color_short(self):
        color = basic.hex_color_short()

        assert re.match(r'[0-9A-F]{3}$', color) is not None

    def test_text(self):
        text1 = basic.text(length=10)
        assert len(text1) == 10

        text2 = basic.text(at_least=10, at_most=15)
        assert len(text2) >= 10 and len(text2) <= 15

        text3 = basic.text(length=26, lowercase=False, uppercase=True,
                           digits=False, spaces=False, punctuation=False)
        assert re.match(r'[A-Z]{26}$', text3) is not None

        text4 = basic.text(length=26, lowercase=True, uppercase=False,
                           digits=False, spaces=False, punctuation=False)
        assert re.match(r'[a-z]{26}$', text4) is not None

        text5 = basic.text(length=10, lowercase=False, uppercase=False,
                           digits=True, spaces=False, punctuation=False)
        assert re.match(r'[0-9]{10}$', text5) is not None

        text6 = basic.text(length=1, lowercase=False, uppercase=False,
                           digits=False, spaces=True, punctuation=False)
        assert text6 == ' '

        text7 = basic.text(length=32, lowercase=False, uppercase=False,
                           digits=False, spaces=False, punctuation=True)
        assert re.match(r"""[!"#$%&\\'()*+,-\.\/:;<=>?@\[\]^_`{|}~]{32}$""",
                        text7) is not None