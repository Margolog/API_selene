import allure
from allure_commons.types import Severity
from requests import Response
from tests.shema.shema import *
from pytest_voluptuous import S


@allure.epic('API reqres.in')
@allure.feature('/api/users')
@allure.severity(Severity.CRITICAL)
@allure.title('Создание пользователя')
@allure.step('Создание пользователя')
def test_create_user(reqres_session):
    name = 'Margo'
    job = 'Doctor'


    result: Response = reqres_session.post(url='/api/users',
                                           json={"name": name, "job": job})

    assert result.status_code == 201, 'Статус код ответа равен 201'

    with allure.step('Проверка полей в ответе'):
        assert result.json()['name'] == name
        assert result.json()['job'] == job
    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(create_user)


@allure.epic('API reqres.in')
@allure.feature('/api/users/2')
@allure.severity(Severity.NORMAL)
@allure.title('Обновление информации о пользователе')
@allure.step('Обновление информации о пользователе')
def test_update_user(reqres_session):
    name = 'Margo'
    job = 'QA'


    result: Response = reqres_session.put(url='/api/users/2',
                                          json={"name": name, "job": job})

    assert result.status_code == 200, 'Статус код ответа равен 201'

    with allure.step('Проверка полей в ответе'):
        assert result.json()['name'] == name
        assert result.json()['job'] == job
    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(update_user)


@allure.epic('API reqres.in')
@allure.feature('/api/unknown/23')
@allure.severity(Severity.MINOR)
@allure.title('Поиск незарегистрированного пользователя')
@allure.step('Поиск пользователя')
def test_user_not_found(reqres_session):
    result: Response = reqres_session.get(url='/api/unknown/23')

    assert result.status_code == 404, 'Статус код ответа равен 404'

    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(user_not_found)


@allure.epic('API reqres.in')
@allure.feature('/api/users/2')
@allure.severity(Severity.CRITICAL)
@allure.title('Удаление пользователя')
@allure.step('Удаление пользователя')
def test_delete_user(reqres_session):
    result = reqres_session.delete(url='/api/users/2')

    assert result.status_code == 204, 'Статус код ответа равен 204'


@allure.epic('API reqres.in')
@allure.feature('/api/login')
@allure.severity(Severity.CRITICAL)
@allure.title('Неуспешная авторизация')
@allure.step('Создание пользователя')
def test_register_unsuccessful(reqres_session):
    email = 'peter@klaven'


    result: Response = reqres_session.post(url='/api/login',
                                           json={"email": email})

    assert result.status_code == 400, 'Статус код ответа равен 400'

    with allure.step('Проверка архитектуры ответа'):
        assert result.json() == S(register_unsuccessful)
