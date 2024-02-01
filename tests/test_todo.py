from lib.todo import *
import pytest

def test_task_todo_contains_todo():
    result = task_todo('This contains #TODO')
    assert result is True

def test_task_todo_no_todo():
    result = task_todo('This does not')
    assert result is False

def test_task_todo_empty_string():
    with pytest.raises(Exception) as e:
        task_todo("")
    
    actual = str(e.value)
    expected = "Error empty string!"

    assert actual == expected

