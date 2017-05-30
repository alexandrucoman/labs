"""
REST-api for stats.
"""
import requests

import cherrypy
import client

CONFIG = {
    'global': {
        'server.socket_host': "127.0.0.1",
        'server.socket_port': 8080,
        'log.error_file': "log"
    },
    # '/': {
    #     'request.dispatch': cherrypy.dispatch.MethodDispatcher()
    #     }
}


class App(object):
    """REST api."""
    exposed = True

    def __init__(self):
        self._client = client.ClientREST()

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def posts(self, **kwargs):
        """Nr. de posts."""
        try:
            return {"posts": len(self._client.posts(**kwargs))}
        except (client.ClientError,
                requests.exceptions.HTTPError):
            raise cherrypy.HTTPError(400, "Bad requests.")

    @cherrypy.tools.json_out()
    @cherrypy.expose
    def comments(self, **kwargs):
        """Nr. de comments."""
        try:
            return {"comments": len(self._client.comments(**kwargs))}
        except (client.ClientError,
                requests.exceptions.HTTPError):
            raise cherrypy.HTTPError(400, "Bad requests.")

    @cherrypy.expose
    def index(self):
        """Toate endpoints."""
        # pylint: disable=no-self-use
        cherrypy.response.headers['Content-Type'] = 'text/plain'
        return "\n".join(["posts", "comments"])


if __name__ == "__main__":
    print "Start"
    cherrypy.quickstart(App(), "/", CONFIG)
