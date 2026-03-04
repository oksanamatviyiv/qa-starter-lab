import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_api_is_reachable(api_client):
    """
    Smoke test: confirm the service responds and returns JSON list for /posts.
    Why use api_client?
    - one unified way to call the API
    - base_url lives in config/fixture, not duplicated in tests
    """
    response = api_client.get("/posts")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
