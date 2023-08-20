import docx2txt


def make_list_from_text(text: str):
    lines = list(filter(lambda line: line != '', text.split("\n")))
    return [line for line in lines if not line.endswith(":")]


def get_categories_from_file(filename: str):
    text = docx2txt.process(filename)
    lines = make_list_from_text(text)
    print([line.split('  ') for line in lines])


get_categories_from_file("../категории.docx")

