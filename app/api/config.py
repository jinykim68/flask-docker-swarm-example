from flask import (current_app, request)
from flask.views import MethodView
from flask_rest_api import Blueprint

blp = Blueprint(
    "config", __name__, url_prefix="/config", description="Config blueprint")


@blp.route("/", strict_slashes=False)
class TestAPI(MethodView):
    @blp.response(code=200)
    def get(self):
        current_app.logger.debug("{} {}".format(request.method, request.url_rule))
        return {
            "OPENAPI_VERSION": current_app.config.OPENAPI_VERSION,
            "CACHE_REDIS_URL": current_app.config.CACHE_REDIS_URL,
            "SESSION_TYPE": current_app.config.SESSION_TYPE,
            "SESSION_REDIS": str(current_app.config.SESSION_REDIS),
            "CELERY_BROKER_URL": current_app.config.CELERY_BROKER_URL,
            "CELERY_RESULT_BACKEND": current_app.config.CELERY_RESULT_BACKEND
        }
