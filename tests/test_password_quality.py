# -*- coding: utf-8 -*-

from swissutil.strings import is_acceptable
from swissutil.strings import evaluate_string_for_stuff
from swissutil.strings import rot15


from swissutil.strings import ERROR_MESSAGE, SUCCESS_MESSAGE


def test_is_acceptable():
    # no uppercase
    assert not is_acceptable("testing123")
    # uppercase only first
    assert not is_acceptable("Testing123")
    assert is_acceptable("123Testing")

def test_evaluate_string_for_stuff(capsys):
    #capsys captures sys.stdout and sys.stderr
    assert evaluate_string_for_stuff("123Testing") == 0
    out, err = capsys.readouterr()
    assert out.strip() == SUCCESS_MESSAGE
    assert evaluate_string_for_stuff("123testinG") != 0
    out, err = capsys.readouterr()
    assert out.strip() == ERROR_MESSAGE

def test_evaluate_string_for_stuff_with_mocking(mocker):
    #mocker can be used to *patch* objects so that instead of
    #a real object a MagicMock object is called
    mocked_function = mocker.patch("swissutil.strings.is_acceptable")
    mocked_function.return_value = True
    assert evaluate_string_for_stuff("not_used") == 0
    assert mocked_function.called_once_with("not_used")

    mocked_function.reset_mock()
    mocked_function.return_value = False
    assert evaluate_string_for_stuff("not_used") != 0
    assert mocked_function.called_once_with("not_used")

def test_rot15():
    assert rot15(rot15(u"example")) == u"example"
    assert rot15(rot15(u"åbo")) == u"åbo"

