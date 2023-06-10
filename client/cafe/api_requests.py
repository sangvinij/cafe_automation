from geopy.geocoders import Nominatim

import requests


API_URL = r'http://127.0.0.1:8000/'


def get_list_of_categories():
    response = requests.get(API_URL + r'api/v1/management/menu_categories/')
    data = response.json()
    list_of_menu_categories = [data[i]['category'] for i in range(len(data))]
    return list_of_menu_categories


def get_list_of_links():
    response = requests.get(API_URL + r'api/v1/management/social_media_links/')
    dict_of_social_media = {}
    data = response.json()
    for i in range(len(data)):
        dict_of_social_media.update({data[i]['social_media_name']:
                                    data[i]['social_media_link']})

    return dict_of_social_media


def get_menu_items():
    response = requests.get(API_URL + r'api/v1/management/menu/')
    # data = response
    return response.json()


def get_list_of_addresses():
    response = requests.get(API_URL + r'api/v1/management/cafe_addresses/')
    data = response.json()
    list_of_addresses = [data[i]['cafe_address'] for i in range(len(data))]
    return list_of_addresses


def get_latitude_and_longitude(address):
    geolocator = Nominatim(user_agent="CafeApp")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


def login(phone_number=None, password=None):
    response = requests.post(API_URL + r'auth/token/login/',
                             data={'phone_number': phone_number,
                                   'password': password})
    if not response:
        pass

    token = response.json()['auth_token']
    return token


def get_user(token=None):
    response = requests.get(API_URL + r'auth/users/me',
                            headers={'Authorization': f'Token {token}'})
    return response


def register(phone_number, password,
             first_name=None, last_name=None, email=None):
    response = requests.post(
        API_URL + r'auth/users/', data={
            'phone_number': phone_number,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
    )
    return response


def logout(token):
    response = requests.post(API_URL + r'auth/token/logout/',
                             headers={'Authorization': f'Token {token}'})
    return response
