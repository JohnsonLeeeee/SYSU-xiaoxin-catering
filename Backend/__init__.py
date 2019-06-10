
from flask import Flask
from flask_login import LoginManager
from flask_cache import Cache
from flask_wtf import CsrfProtect
from .Web.index import route_index
from .Web.food import route_food
from .Model.base import db
from .libs.email import mail
from .libs.UrlManager import UrlManager

login_manager = LoginManager()
cache = Cache(config={'CACHE_TYPE': 'simple'})

def register_plugin(app):
    from .Model.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

def register_web_blueprint(app):
    from .Web import web
    app.register_blueprint(route_index)
    app.register_blueprint(route_food)

def create_app(config=None):
    app = Flask(__name__, template_folder="template",static_folder="static")

    #: load default configuration
    app.config.from_object('Backend.Config.settings')
    app.config.from_object('Backend.Config.secure')

    register_plugin(app)

    # 注册email模块
    mail.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    cache.init_app(app)

    #注册CSRF保护
    csrf = CsrfProtect()
    csrf.init_app(app)

    register_web_blueprint(app)

    app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
    app.add_template_global(UrlManager.buildUrl, 'buildUrl')

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app
