import pytest
import json

from converter import convert_to_html

HTML_STRING = """<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>"""


def get_data():
    with open("source.json") as j_file:
        data = json.load(j_file)
    return data


def test_converter():
    data = get_data()
    output_code = convert_to_html(data)
    assert output_code == HTML_STRING
