from api_requests import create_pet, get_pet_by_id, update_pet, delete_pet, find_pets_by_status
import test_data



# Глобальная переменная для хранения ID созданного питомца
created_pet_id = None

# Тест создания животного (POST)
def test_create_pet():
    global created_pet_id  # Используем глобальную переменную
    response = create_pet(test_data.create_pet_body)
    assert response.status_code == 200  # Проверка успешного создания
    created_pet_id = response.json().get("id")  # Сохраняем ID для дальнейших тестов
    assert created_pet_id is not None  # Проверка наличия ID для созданного животного

# Тест получения животного (GET)
def test_get_pet():
    test_create_pet()  # Создаем животное, чтобы получить его ID
    response = get_pet_by_id(created_pet_id)
    assert response.status_code == 200  # Проверка успешного получения
    assert response.json().get("name") == test_data.create_pet_body["name"]

# Тест поиска питомцев по статусу (GET)
def test_find_pets_by_status():
    response = find_pets_by_status("available")
    assert response.status_code == 200  # Проверка успешного получения питомцев
    assert isinstance(response.json(), list)  # Проверка, что это список

# Тест обновления животного (PUT)
def test_update_pet():
    test_create_pet()  # Создаем животное, чтобы получить его ID
    test_data.update_pet_body["id"] = created_pet_id  # Устанавливаем ID для обновления
    response = update_pet(test_data.update_pet_body)
    assert response.status_code == 200  # Проверка успешного обновления
    assert response.json().get("status") == test_data.update_pet_body["status"]

# Тест удаления животного (DELETE)
def test_delete_pet():
    test_create_pet()  # Создаем животное, чтобы получить его ID
    response = delete_pet(created_pet_id)
    assert response.status_code == 200  # Проверка успешного удаления

# Дополнительные тесты для всевозможных сценариев
def test_create_invalid_pet():
    response = create_pet(test_data.invalid_pet_body)
    assert response.status_code == 400  # Проверка на ошибку при создании

def test_update_nonexistent_pet():
    test_data.update_pet_body["id"] = 99999  # Неверный ID
    response = update_pet(test_data.update_pet_body)
    assert response.status_code == 404  # Проверка, что обновление не удалось

def test_find_pets_by_invalid_status():
    response = find_pets_by_status("unknown_status")
    assert response.status_code == 400  # Проверка на ошибку при неправильном статусе

def test_delete_nonexistent_pet():
    response = delete_pet(99999)  # Неверный ID
    assert response.status_code == 404  # Проверка, что удалить не удалось

def test_create_pet_with_existing_id():
    test_create_pet()  # Создаем нового питомца и получаем его ID
    test_data.create_pet_body["id"] = created_pet_id  # Устанавливаем тот же ID для нового питомца
    response = create_pet(test_data.create_pet_body)
    assert response.status_code == 409  # Код 409 - конфликт
