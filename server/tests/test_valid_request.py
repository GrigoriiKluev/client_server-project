from datetime import datetime
import pytest
from protocol import validate_request


@pytest.fixture
def action_fixture():
    return 'test'

@pytest.fixture
def time_fixture():
    return datetime.now().timestamp()

@pytest.fixture
def data_fixture():
    return 'message'

@pytest.fixture
def request_fixture(action_fixture,time_fixture, data_fixture):
    return {
        'action': action_fixture,
        'time': time_fixture,
        'data': data_fixture
    }






def test_valid_request(request_fixture):
    valid = validate_request(request_fixture)
    assert valid == True
