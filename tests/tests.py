from unittest import result

import allure
from allure_commons.types import Severity
from requests import Response
from tests.shema.shema import *
from pytest_voluptuous import S


@allure.epic('Test API')
@allure.feature('POST запрос')
@allure.severity(Severity.CRITICAL)
@allure.title('Создание пользователя')
@allure.step('Запрос для создания пользователя')
def test_create_user(reqres_session):
    name = 'Margo'
    job = 'Doctor'

    result: Response = reqres_session.post(url='/api/users',
                                           json={"name": name, "job": job})
    with allure.step('Проверка статус кода'):
        assert result.status_code == 201
    with allure.step('Проверка полей в ответе'):
        assert result.json()['name'] == name
        assert result.json()['job'] == job
    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(create_user)


@allure.epic('Test API')
@allure.feature('PUT запрос')
@allure.severity(Severity.NORMAL)
@allure.title('Обновление информации о пользователе')
@allure.step('Запрос для обновления информации о пользователе')
def test_update_user(reqres_session):
    name = 'Margo'
    job = 'QA'

    result: Response = reqres_session.put(url='/api/users/2',
                                          json={"name": name, "job": job})
    with allure.step('Проверка статус кода'):
        assert result.status_code == 200
    with allure.step('Проверка полей в ответе'):
        assert result.json()['name'] == name
        assert result.json()['job'] == job
    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(update_user)


@allure.epic('Test API')
@allure.feature('GET запрос')
@allure.severity(Severity.MINOR)
@allure.title('Поиск незарегистрированного пользователя')
@allure.step('Пользователь не найден')
def test_user_not_found(reqres_session):
    result: Response = reqres_session.get(url='/api/unknown/23')

    with allure.step('Проверка статус кода'):
        assert result.status_code == 404
    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(user_not_found)


@allure.epic('Test API')
@allure.feature('DELETE запрос')
@allure.severity(Severity.CRITICAL)
@allure.title('Удаления пользователя')
@allure.step('Запрос для удаления пользователя')
def test_delete_user(reqres_session):
    result = reqres_session.delete(url='/api/users/2')

    with allure.step('Проверка статус кода'):
        assert result.status_code == 204


@allure.epic('Test API')
@allure.feature('POST запрос')
@allure.severity(Severity.CRITICAL)
@allure.title('Неуспешная авторизация')
@allure.step('Запрос для создания пользователя')
def test_register_unsuccessful(reqres_session):
    email = 'peter@klaven'
    result: Response = reqres_session.post(url='/api/login',
                                           json={"email": email})

    with allure.step('Проверка статус кода'):
        assert result.status_code == 400
    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(register_unsuccessful)
