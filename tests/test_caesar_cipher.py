# -*- coding: utf-8 -*-

"""Tests for the Caesar Cipher module"""
from swissutil.caesar_cipher import rot15

def test_rot15():
    assert rot15(rot15(u"example")) == u"example"
    assert rot15(rot15(u"åbo")) == u"åbo"
    assert rot15(u"tromsø") == u"ecøädo"
