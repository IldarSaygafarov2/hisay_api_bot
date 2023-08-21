import docx2txt
import re


def make_list_from_text(text: str):
    lines = list(filter(lambda line: line != '', text.split("\n")))
    return [line for line in lines if not line.endswith(":")]


def get_categories_from_file(filename: str):
    text = docx2txt.process(filename)
    lines = make_list_from_text(text)
    result = {}

    for line in lines:

        tags = re.findall(r'#[a-zа-яё_-]+', line)
        for tag in tags:
            if tag in line:
                line = line.replace(tag, '').strip()
        result[line] = tags

    return result



