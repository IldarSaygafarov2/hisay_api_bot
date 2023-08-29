import requests

from tg_bot.data.config import BASE_URL


def get_services():
    endpoint = BASE_URL + '/services'
    response = requests.get(endpoint).json()
    return response


def get_service_id(name):
    endpoint = BASE_URL + '/services/' + name
    service_id = requests.get(endpoint).json()
    return service_id


def create_service_profile(service_data, file):
    endpoint = BASE_URL + '/service-profile/create'
    file_data = {'document_photo': file}
    s = requests.post(endpoint, data=service_data, files=file_data)
    print(s.text)
    print('service created')
