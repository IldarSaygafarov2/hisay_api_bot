import requests


def get_files_bytes(file_url):
    return requests.get(file_url).content
