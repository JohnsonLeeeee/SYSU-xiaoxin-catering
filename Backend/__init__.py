
from flask import Flask
from flask_login import LoginManager
from flask_cache import Cache
from flask_wtf import CsrfProtect
from .Web.index import route_index
from .Web.food import route_food
from .Web.comment import route_comment
from .Web.finance import route_finance
from .Web.upload import route_upload
from .Web.Login import route_user
from .Web.Stat import route_stat
from .Web.chart import route_chart
from .API.V1 import create_blueprint_v1
from .Web.auth import web
from .Model.base import db
from .Model.user import User
from .Model.Comment import Comment
from .Model.Cart import Cart
from .Model.restaurant import Restaurant
from .Model.Order import Order
from .libs.email import mail
from .libs.web_help import MyJSONEncoder, dispatch_coupon
from .libs.UrlManager import UrlManager
import datetime

login_manager = LoginManager()
cache = Cache(config={'CACHE_TYPE': 'simple'})

def create_restaurant(db):
    order1 = Order()
    order1.pay_time = datetime.datetime.now() + datetime.timedelta(days=-1)
    order1.total_price = 10
    order1.uid = 1
    order1.pay_price = 10
    order1.rid = 1
    order1.note = "null"

    order2 = Order()
    order2.pay_time = datetime.datetime.now()
    order2.total_price = 80
    order2.uid = 1
    order2.pay_price = 70
    order2.rid = 1
    order2.note = "null"

    comment1 = Comment()
    comment1.uid = 1
    comment1.rid = 1
    comment1.content = "cxknmsl"

    cart1 = Cart()
    cart1.uid = 1
    cart1.did = 1
    cart1.quantity = 2
    cart1.orderid = 1

    res = Restaurant()
    res.name = "GOGO"
    coupon = dispatch_coupon(1,1)
    with db.auto_commit():
        db.session.add(coupon)
        # db.session.add(order1)
        # db.session.add(order2)
        # db.session.add(comment1)
        db.session.add(cart1)

    if Restaurant.query.filter_by(name = res.name).first():
        return

    with db.auto_commit():
        db.session.add(res)

def register_plugin(app):
    from .Model.base import db
    from .Model.Order import Order
    from .Model.Dish import Dish
    from .Model.Cart import Cart
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_restaurant(db)


def register_web_blueprint(app):
    app.register_blueprint(route_index)
    app.register_blueprint(route_food)
    app.register_blueprint(route_comment)
    app.register_blueprint(route_finance)
    app.register_blueprint(route_stat)
    app.register_blueprint(route_chart)
    app.register_blueprint(web,url_prefix = "/web")
    app.register_blueprint(route_user,url_prefix = "/user" )
    app.register_blueprint(route_upload, url_prefix="/upload")
    app.register_blueprint(create_blueprint_v1(),url_prefix="/v1")

def create_app(config=None):
    app = Flask(__name__, template_folder="template",static_folder="static")
    app.json_encoder = MyJSONEncoder
    #: load default configuration
    app.config.from_object('Backend.Config.settings')
    app.config.from_object('Backend.Config.secure')

    register_plugin(app)
    # 注册email模块
    mail.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    cache.init_app(app)

    #注册CSRF保护
    # csrf = CsrfProtect()
    # csrf.init_app(app)

    register_web_blueprint(app)

    app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
    app.add_template_global(UrlManager.buildUrl, 'buildUrl')

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    return app
