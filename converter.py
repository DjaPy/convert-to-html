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


def convert_to_html(data):
    html_str = ""
    for simple_dict in data:
        h1 = simple_dict['title']
        p = simple_dict['body']
        line = "<h1>{text_h1}</h1><p>{text_p}</p>".format(text_h1=h1, text_p=p)
        html_str += line
    return html_str


def write_html_to_file(data, file):
    with open(file, 'w') as w_file:
        w_file.write(data)


def main():
    r_file = "source.json"
    w_file = "index.html"
    json_text = get_json(r_file)
    convert_data = convert_to_html(json_text)
    write_html_to_file(convert_data, w_file)
    print("Conversion successful")


if __name__ == "__main__":
    main()
