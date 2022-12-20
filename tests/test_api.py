import allure
from allure_commons.types import Severity
from tests.shema.shema import *
from pytest_voluptuous import S

from utils.allure_labels import allure_labels


@allure.severity(Severity.CRITICAL)
def test_create_user(reqres_session):
    name = 'Margo'
    job = 'Doctor'
    allure_labels(feature='API reqres.in',
                  story='Пользователь /api/users',
                  title='Создание пользователя')

    result = reqres_session.post(url='/api/users',
                                 json={"name": name, "job": job})

    assert result.status_code == 201, f'Ошибка HTTP {result.status_code}'
    assert result.json()['name'] == name, f'Поле name != {name}'
    assert result.json()['job'] == job, f'Поле job != {job}'
    assert result.json() == S(create_user), 'Ответ не соответствует схеме'


@allure.severity(Severity.NORMAL)
def test_update_user(reqres_session):
    name = 'Margo'
    job = 'QA'
    allure_labels(feature='API reqres.in',
                  story='Пользователь /api/users',
                  title='Обновление информации о пользователе')

    result = reqres_session.put(url='/api/users/2',
                                json={"name": name, "job": job})

    assert result.status_code == 200, f'Ошибка HTTP {result.status_code}'
    assert result.json()['name'] == name, f'Поле name != {name}'
    assert result.json()['job'] == job, f'Поле job != {job}'
    assert result.json() == S(update_user), 'Ответ не соответствует схеме'


@allure.severity(Severity.MINOR)
def test_user_not_found(reqres_session):
    allure_labels(feature='API reqres.in',
                  story='Неизвестный пользователь /api/unknown',
                  title='Поиск незарегистрированного пользователя')

    result = reqres_session.get(url='/api/unknown/23')

    assert result.status_code == 404, f'Пришел неожиданный ответ {result.status_code}'
    assert result.json() == S(user_not_found), 'Ответ не соответствует схеме'


@allure.severity(Severity.CRITICAL)
def test_delete_user(reqres_session):
    allure_labels(feature='API reqres.in',
                  story='Пользователь /api/users',
                  title='Удаление пользователя')

    result = reqres_session.delete(url='/api/users/2')

    assert result.status_code == 204, f'Ошибка HTTP {result.status_code}'


@allure.severity(Severity.CRITICAL)
def test_register_unsuccessful(reqres_session):
    email = 'peter@klaven'
    allure_labels(feature='API reqres.in',
                  story='Авторизация /api/login',
                  title='Неуспешная авторизация')

    result = reqres_session.post(url='/api/login',
                                 json={"email": email})

    assert result.status_code == 400, f'Пришел неожиданный ответ {result.status_code}'
    assert result.json() == S(register_unsuccessful), 'Ответ не соответствует схеме'
