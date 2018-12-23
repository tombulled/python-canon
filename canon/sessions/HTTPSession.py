import requests

"""
Imports:
    requests

Contains:
    <HTTPSession>
"""

class HTTPSession(requests.Session):
    """
    Wrapper for: <requests.Session>
    """

    def __init__(self, *args, **kwargs):
        """
        Initialise self and super
        """

        super().__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        """
        Wrapper for super().get

        Note: 'verify' defaults to False
        """

        kwargs.setdefault('verify', False)

        resp = super().get(*args, **kwargs)

        return resp

    def post(self, *args, **kwargs):
        """
        Wrapper for super().post

        Note: 'verify' defaults to False
        """

        kwargs.setdefault('verify', False)

        resp = super().post(*args, **kwargs)

        return resp
