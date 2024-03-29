# В проекте автоматизирована проверка API ресурса <a target="_blank" href="https://reqres.in/">reqres.in</a>

## :open_book: Содержание:
- [Технологии и инструменты](#gear-в-проекте-используются-следующие-технологии-и-инструменты)
- [Что проверяем](#heavy_check_mark-что-проверяем)
- [Запуск тестов из Jenkins](#-запуск-тестов-из-jenkins)
- [Отчеты](#bar_chart-отчеты-о-прохождении-тестов-доступны-в-allure)
- - [Allure](#-allure)
- - [Telegram](#-telegram)
- - [Allure TestOps](#-проект-интегрирован-с-allure-testOps)

## :gear: В проекте используются следующие технологии и инструменты:
<p align="center">
<img width="5%" title="Python" src="https://github.com/Margolog/diplom_API/blob/master/resources/python.png">
<img width="6%" title="Pytest" src="https://github.com/Margolog/diplom_API/blob/master/resources/pytest.png">
<img width="5%" title="PyCharm" src="https://github.com/Margolog/diplom_API/blob/master/resources/pycharm.png">
<img width="6%" title="Jenkins" src="https://github.com/Margolog/diplom_API/blob/master/resources/jenkins.svg">
<img width="6%" title="Allure TestOps" src="https://github.com/Margolog/diplom_API/blob/master/resources/AllureTestOps.png">
<img width="6%" title="Allure" src="https://github.com/Margolog/diplom_API/blob/master/resources/allure.svg">
<img width="6%" title="Selene" src="https://github.com/Margolog/diplom_API/blob/master/resources/selene.png">
<img width="6%" title="Telegram" src="https://github.com/Margolog/diplom_API/blob/master/resources/tg.svg">
</p>


## :heavy_check_mark: Описание
В проекте автоматизирована проверка API reqres.in.

## :heavy_check_mark: Что проверяем

> - Создание пользователя;
> - Обновление информации о пользователе;
> - Поиск незарегистрированного пользователя;
> - Удаления пользователя;
> - Неуспешная авторизация.

## Сборка в [Jenkins](https://jenkins.autotests.cloud/job/002-Margologu-API/)
<p align="center">
  <img src="resources/images/jenkins.jpg" alt="Jenkins"/>
</p>

## Информация о тестах в [Allure report](https://jenkins.autotests.cloud/job/002-Margologu-API/allure/)
<p align="center">
  <img src="resources/images/Allure.jpg" alt="Allure report"/>
</p>


### Окно с кейсами
<p align="center">
  <img src="resources/images/allure_cases.jpg" alt="Allure report"/>
</p>


#### Графики
<p align="center">
  <img src="resources/images/allure_graphs.jpg" alt="Allure report"/>
</p>

## Интеграция с [Allure TestOps](https://allure.autotests.cloud/launch/17672/tree?search=W3siaWQiOiJzdGF0dXMiLCJ0eXBlIjoidGVzdFN0YXR1c0FycmF5IiwidmFsdWUiOlsicGFzc2VkIl19XQ%3D%3D&treeId=0)

### Тест-кейсы
<p align="center">
  <img src="resources/images/test_cases.jpg" alt="Allure TestOps"/>
</p>

### Дашборд
<p align="center">
  <img src="resources/images/dashboards.jpg" alt="Allure TestOps"/>
</p>


## Интеграция с [Jira](https://jira.autotests.cloud/browse/HOMEWORK-470)
<p align="center">
  <img src="resources/images/jira.jpg" alt="Jira"/>
</p>

## Уведомление в Telegram
<p align="center">
  <img src="resources/images/telegram.jpg" alt="Telegram notification"/>
</p>

