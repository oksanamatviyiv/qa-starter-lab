import pytest


@pytest.mark.api
def test_single_post_has_required_fields(api_client):
    """
    Contract test: /posts/1 returns a post object with required keys.
    Keep the list of required keys in one place to avoid mismatch across tests.
    """
    r = api_client.get("/posts/1")
    assert r.status_code == 200

    post = r.json()
    for key in ("userId", "id", "title", "body"):
        assert key in post


@pytest.mark.api
def test_unknown_post_returns_404(api_client):
    """
    Negative test: unknown resource should return 404.
    """
    r = api_client.get("/posts/999999")
    assert r.status_code == 404
