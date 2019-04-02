
from flask import Flask
from flask_login import LoginManager
from flask_cache import Cache
from Model.base import db
from libs.email import mail

login_manager = LoginManager()
cache = Cache(config={'CACHE_TYPE': 'simple'})


def register_web_blueprint(app):
    from Web import web
    app.register_blueprint(web)

def create_app(config=None):
    app = Flask(__name__)

    #: load default configuration
    app.config.from_object('Config.settings')
    app.config.from_object('Config.secure')

    db.init_app(app)

    # 注册email模块
    mail.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    cache.init_app(app)

    # 注册CSRF保护
    # csrf = CsrfProtect()
    # csrf.init_app(app)

    register_web_blueprint(app)

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app
