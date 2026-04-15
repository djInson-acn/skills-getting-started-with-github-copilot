import copy

import pytest
from httpx import Client

from src import app as app_module


@pytest.fixture
def client():
    with Client(app=app_module.app, base_url="http://testserver") as client:
        yield client


@pytest.fixture(autouse=True)
def reset_activities():
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)
