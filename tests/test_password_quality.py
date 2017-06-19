# -*- coding: utf-8 -*-

from swissutil.password_quality import is_acceptable
from swissutil.password_quality import evaluate_password_quality
from swissutil.caesar_cipher import rot15
from swissutil.password_quality import has_numbers
from swissutil.password_quality import has_upper
from swissutil.password_quality import has_lower

def test_is_acceptable():
    # no uppercase
    assert not is_acceptable("testing123")
    # uppercase only first
    assert not is_acceptable("Testing123")
    assert is_acceptable("123Testing")
    assert not is_acceptable("TEstINGestING")
    assert not is_acceptable("1234567899")
    assert not is_acceptable("aTa1g")


def test_evaluate_password_quality():
    assert evaluate_password_quality("123Testing") == 0
    assert evaluate_password_quality("123testinG") != 0


def test_evaluate_password_quality_with_mocking(mocker):
    # mocker can be used to *patch* objects so that instead of
    # a real object a MagicMock object is called.
    # The MagicMock can be e.g. configured to return a value when called
    # to isolate a function from another one.
    mocked_function = mocker.patch("swissutil.password_quality.is_acceptable")
    mocked_function.return_value = True
    assert evaluate_password_quality("not_used") == 0
    assert mocked_function.called_once_with("not_used")

    mocked_function.reset_mock()
    mocked_function.return_value = False
    assert evaluate_password_quality("not_used") != 0
    assert mocked_function.called_once_with("not_used")


def test_has_numbers():
    assert has_numbers("12345")
    assert not has_numbers("foobar")
    assert not has_numbers("12foobar34", ignore_chars=2)
    assert  has_numbers("12foobar34", ignore_chars=1)


def test_has_lower():
    assert has_lower("foobar")
    assert not has_lower("12345ASGASGAGS")
    assert not has_lower("foBAAAR12ar", ignore_chars=2)
    assert  has_lower("foBAAAR12ar", ignore_chars=1)


def test_has_upper():
    assert has_upper("foobar")
    assert not has_upper("12345ASGASGAGS")
    assert not has_upper("foBAAAR12ar", ignore_chars=2)
    assert  has_upper("foBAAAR12ar", ignore_chars=1)
