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
    requests.post(endpoint, data=service_data, files=file)


def get_service_profiles_ids():
    endpoint = BASE_URL + "/service-profiles/ids/"
    result = requests.get(endpoint).json()
    return result


def get_simple_users_profiles_ids():
    endpoint = BASE_URL + "/simple-users-profiles/ids/"
    result = requests.get(endpoint).json()
    return result


def create_simple_user(user_data):
    endpoint = BASE_URL + "/users/create/"
    resp = requests.post(endpoint, data=user_data)
    print(resp.text)