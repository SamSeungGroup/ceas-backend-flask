from flask import Flask
from sqlalchemy import create_engine

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")
    database = create_engine(app.config['DB_URL'])
    app.database = database

    from .views import comment_positive_view, word_cloud_view
    app.register_blueprint(comment_positive_view.bp)
    app.register_blueprint(word_cloud_view.bp)

    return app