# test_data.py

# Пример тела запроса для создания питомца
create_pet_body = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "Dog"
    },
    "name": "doggie",
    "photoUrls": ["https://example.com/dog.jpg"],  # Пример фото
    "tags": [{"id": 1, "name": "healthy"}],
    "status": "available"
}

# Пример тела запроса для обновления питомца
update_pet_body = {
    "id": 0,  # Этот ID будет обновлен в тестах
    "category": {
        "id": 1,
        "name": "Dog"
    },
    "name": "doggie updated",
    "photoUrls": ["https://example.com/dog_updated.jpg"],  # Новый пример фото
    "tags": [],
    "status": "sold"
}

# Пример тела запроса для создания питомца с ошибками
invalid_pet_body = {
    "id": -1,  # Неверный ID
    "category": {
        "id": 1,
        "name": "Cat"
    },
    "name": "",  # Пустое имя
    "photoUrls": [],  # Пустое поле для фото
    "tags": [],
    "status": "available"
}
