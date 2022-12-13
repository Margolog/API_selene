import allure
import pytest
from _pytest.fixtures import FixtureRequest
from utils.base_user import BaseSession


@pytest.fixture(scope='session')
def reqres_session():
    with BaseSession(base_url='https://reqres.in') as session:
        yield session


@pytest.fixture(scope='session')
def lambda_steps(request: FixtureRequest):
    allure.dynamic.title(" ".join(request.node.name.split("_")[1:]).capitalize())
