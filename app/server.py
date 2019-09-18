import logging

from app import (create_app, create_celery)

app = create_app('app.config.Config')

if __name__ != '__main__':
    # Use gunicorn to run the app. We need to have a logger to display logs.
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

celery = create_celery(app=app)

if __name__ == '__main__':
    # Use the embedded server to run (e.g., FLASK_APP=server.py flask run).
    from app.ext import socket_io
    socket_io.run(app=app, debug=True)
