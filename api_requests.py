# api_requests.py

import requests
import config

# Функция: создать животное (POST)
def create_pet(pet_body):
    response = requests.post(config.BASE_URL + config.PET_ENDPOINT, json=pet_body)
    return response

# Функция: получить животное по ID (GET)
def get_pet_by_id(pet_id):
    response = requests.get(config.BASE_URL + config.PET_ENDPOINT + f"/{pet_id}")
    return response

# Функция: обновить животное (PUT)
def update_pet(pet_body):
    response = requests.put(config.BASE_URL + config.PET_ENDPOINT, json=pet_body)
    return response

# Функция: удалить животное (DELETE)
def delete_pet(pet_id):
    response = requests.delete(config.BASE_URL + config.PET_ENDPOINT + f"/{pet_id}")
    return response

# найти питомцев по статусу (GET)
def find_pets_by_status(status):
    response = requests.get(config.BASE_URL + config.PET_ENDPOINT + "/findByStatus", params={"status": status})
    return response
