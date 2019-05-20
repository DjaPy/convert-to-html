import pytest
import json

from converter import convert_to_html

HTML_STRING = """<h3>Title #1</h3><div>Hello, World 1!</div>"""


def get_data():
    with open("source.json") as j_file:
        data = json.load(j_file)
    return data


def test_converter():
    data = get_data()
    output_code = convert_to_html(data)
    assert HTML_STRING in output_code