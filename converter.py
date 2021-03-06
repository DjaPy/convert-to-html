import json


def get_json(file):
    try:
        with open(file) as json_f:
            data = json.load(json_f)
        return data
    except ValueError as e:
        print(
            "{0}"
            "Most likely you are loading not json file. Download the file "
            "with the correct extension".format(e)
        )


def check_array(data):
    if isinstance(data, list):
        return True


def wrap_tag(simple_dict):
    wrap_line = ""
    for tag_key, body_value in simple_dict.items():
        tag = tag_key
        body = body_value
        line = "<{tag}>{body}</{tag}>".format(tag=tag, body=body)
        wrap_line += line
    return wrap_line


def convert_to_html(data, array=True):
    if array:
        html_list_str = ""
        for simple_dict in data:
            wrap_line = wrap_tag(simple_dict)
            list_wrap_line = "<li>{body_li}</li>".format(body_li=wrap_line)
            html_list_str += list_wrap_line
        return "<ul>{body_list}</ul>".format(body_list=html_list_str)
    else:
        html_str = ""
        for simple_dict in data:
            wrap_line = wrap_tag(simple_dict)
            html_str += wrap_line
        return html_str


def write_html_to_file(data, file):
    with open(file, 'w') as w_file:
        w_file.write(data)


def main():
    r_file = "source.json"
    w_file = "index.html"
    json_text = get_json(r_file)
    array = check_array(json_text)
    convert_data = convert_to_html(json_text, array)
    write_html_to_file(convert_data, w_file)
    print("Conversion successful")


if __name__ == "__main__":
    main()
