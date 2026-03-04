import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        # remove any trailing slash to avoid double-slash when
        # joining with endpoints later
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, endpoint: str, **kwargs):
        # build the full URL by combining base_url and endpoint
        url = f"{self.base_url}/{endpoint.lstrip('/') }"
        # delegate to requests; timeout prevents hanging tests
        return requests.get(url, timeout=self.timeout, **kwargs)
    
    '''
    **kwargs means:
    “Collect all extra keyword arguments into a dictionary.”
    This allows the caller to pass any additional parameters that requests.get() accepts, such as headers, params, etc., without having to explicitly define them in the APIClient method signature.
    '''    
