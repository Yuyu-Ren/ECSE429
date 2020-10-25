import requests
import json
from support.assertions import assert_valid_json_schema, assert_valid_dictionary_schema, \
    get_valid_dictionary_schema


def test_get_projects_return_code():
    r = requests.get(url="http://localhost:4567/projects")
    assert r.status_code == 200


def test_get_projects_return_payload():
    r = requests.get(url="http://localhost:4567/projects")
    assert assert_valid_json_schema(r.json(), 'projects.get.json')


def test_head_projects_return_code():
    r = requests.get(url="http://localhost:4567/projects")
    assert r.status_code == 200


def test_head_projects_return_payload():
    r = requests.head(url="http://localhost:4567/projects")

    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False


def test_head_projects_headers():
    r = requests.head(url="http://localhost:4567/projects").headers
    assert r['Server'] == get_valid_dictionary_schema('projects.head.json')['Server'] and \
           r['Content-Type'] == get_valid_dictionary_schema('projects.head.json')['Content-Type'] and \
           r['Transfer-Encoding'] == get_valid_dictionary_schema('projects.head.json')['Transfer-Encoding']




