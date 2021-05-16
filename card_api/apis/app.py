import os as _os
from uuid import uuid4
import connexion as _connexion
import flask as _flask
import connexion.apps.flask_app as _flask_app
import enum as _enum


class CardGameEncoder(_flask_app.FlaskJSONEncoder):
    def default(self, o):
        if isinstance(o, _enum.Enum):
            return o.value
        if isinstance(o, object):
            return o.__dict__
        if isinstance(o, uuid4):
            return str(o)
        return super().default(o)


def create_app():
    options = {"swagger_url": "/ui"}
    connexion_app = _connexion.App(__name__, options=options)
    _flask.WEBAPP = connexion_app
    flask_app = connexion_app.app
    connexion_app.app.json_encoder = CardGameEncoder
    connexion_app.add_api(
        "specifications.yaml",
        base_path="/api/v1",
        validate_responses=True,
        strict_validation=True,
        resolver=_connexion.RestyResolver("cms_rest_api"),
    )
    return flask_app
