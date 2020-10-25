import requests
import json
import pytest

def test_get_todos_return_code():
    r = requests.get(url="http://localhost:4567/todos")
    assert r.status_code == 200


def test_get_todos_with_id_return_code():
    r = requests.get(url="http://localhost:4567/todos/1")
    assert r.status_code == 200


def test_get_project_with_todo_id_return_code():
    r = requests.get(url="http://localhost:4567/todos/1/tasksof")
    assert r.status_code == 200


def test_get_doc_return_code():
    r = requests.get(url="http://localhost:4567/docs")
    assert r.status_code == 200

