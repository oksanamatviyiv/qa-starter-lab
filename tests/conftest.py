import pytest
from config import BASE_URL, DEFAULT_TIMEOUT
from src.api.client import APIClient


@pytest.fixture(scope="session")
def api_client():
    """
    Create one APIClient for the whole test session.
    Session scope is fine because the client is stateless (just HTTP calls).
    """
    return APIClient(BASE_URL, timeout=DEFAULT_TIMEOUT)
