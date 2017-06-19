# -*- coding: utf-8 -*-

"""Tests for the Caesar Cipher module"""


def test_rot15():
    assert rot15(rot15(u"example")) == u"example"
    assert rot15(rot15(u"åbo")) == u"åbo"
