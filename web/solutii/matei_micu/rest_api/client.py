""""
Client for `https://jsonplaceholder.typicode.com/`
"""
import urllib

import requests

DEFAULT_URL = "https://jsonplaceholder.typicode.com/"

class ClientError(Exception):
    """Base exception for the JSON Placeholder Client."""
    pass



class ClientREST(object):
    """REST client."""
    def __init__(self, base_url=DEFAULT_URL):
        self._base_url = base_url

    def _request(self, method, resource, data=None):
        """Send a request to the API."""
        url = requests.compat.urljoin(self._base_url, resource)
        try:
            response = requests.request(method=method, url=url,
                                        data=data)

            # NOTE(mmicu): If HTTPError is raise we want to propagate it
            response.raise_for_status()
        except requests.exceptions.ConnectionError as ex:
            raise ClientError(ex)

        try:
            return response.json()
        except (ValueError, TypeError) as ex:
            raise ClientError(ex)

    def _get(self, resource):
        """Get the required resource."""
        return self._request("GET", resource)

    def _post(self, resource, data):
        """Create a new resource."""
        return self._request("POST", resource, data)

    def _put(self, resource, data):
        """Update an existing resource."""
        return self._request("PUT", resource, data)

    def _delete(self, resource):
        """Delete the required resource."""
        return self._request("DELETE", resource)

    def posts(self, **kwargs):
        """Return all the posts."""
        url = "/posts"
        if kwargs:
            url += "?{data}".format(data=urllib.urlencode(kwargs))
        return self._get(url)

    def post(self, post_id):
        """Return a post

        :param post_id: The post ID
        """
        return self._get("/posts/{post_id}".format(post_id=post_id))

    def comments(self, **kwargs):
        """Get all comments."""
        url = "/comments"
        url += "?{data}".format(data=urllib.urlencode(kwargs))
        return self._get(url)

    def comment(self, comment_id):
        """Return a comment

        :param comment_id: The comment ID
        """
        return self._get("/comments/{comment_id}".format(
            comment_id=comment_id))

