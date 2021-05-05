from flask import Flask, jsonify
from flask_restful import Api
from app.extension.db import db
from app.api.resources import api_v1_0_bp
from app.extension.ext import ma, migrate, cache
from .config.default import Config
from app.extension.jwt_ext import authenticate, identity
from flask_jwt import JWT

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    #migrate.init_app(app, db)

    Api(app)
    jwt = JWT(app, authenticate, identity)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False
    # Registra los blueprints
    app.register_blueprint(api_v1_0_bp)
    # Registra manejadores de errores personalizados
    register_error_handlers(app)
    return app

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500
    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405
    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404
