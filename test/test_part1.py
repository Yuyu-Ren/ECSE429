import requests
import json
import pytest

const_file = open('test/resources/test1-constants.json',) 
TEST1_CONSTANTS = json.load(const_file)


def test_get_todos_return_code():
    r = requests.get(url="http://localhost:4567/todos")
    assert r.status_code == 200

def test_get_todos_return_payload():
    r = requests.get(url="http://localhost:4567/todos")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_GET_TODO']

def test_get_todos_with_id_return_code():
    r = requests.get(url="http://localhost:4567/todos/1")
    assert r.status_code == 200

def test_get_todos_return_payload():
    r = requests.get(url="http://localhost:4567/todos/1")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_GET_WITH_ID_TODO']

def test_get_project_with_todo_id_return_code():
    r = requests.get(url="http://localhost:4567/todos/1/tasksof")
    assert r.status_code == 200


def test_get_doc_return_code():
    r = requests.get(url="http://localhost:4567/docs")
    assert r.status_code == 200

def test_post_todos_return_code():
    data = TEST1_CONSTANTS['NEW_TODO']
    r = requests.post(url="http://localhost:4567/todos", json=data)
    assert r.status_code == 201


def test_post_todos_with_id_return_code():
    data = TEST1_CONSTANTS['UPDATE_TODO']
    r = requests.post(url="http://localhost:4567/todos/1", json=data)
    assert r.status_code == 200
