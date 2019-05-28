from flask import Flask
from .libs.web_help import ops_render
from .Service.Restaurant import RestaurantService
from .libs.UrlManager import UrlManager
from Backend import create_app

app = create_app()
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')

@app.route("/")
def index():
    resp_data = {
        'data':{
            'finance':{
                'total':0,
                'today':0,
                'month':0
            },
            'coupon': {
                'month_new': 0,
                'total': 0
            },
            'order': {
                'today': 0,
                'month': 0
            },
            'shared': {
                'today': 0,
                'month': 0
            },
        }
    }
    data = resp_data['data']
    data['finance']['month'] = RestaurantService.get_month_pay
    data['coupon']['month_new'] = RestaurantService.get_month_coupon
    data['finance']['total'] = RestaurantService.get_today_pay
    data['order']['month'] = RestaurantService.get_month_order
    data['shared']['month'] = RestaurantService.get_month_share
    data['finance']['today'] = RestaurantService.get_today_pay
    data['coupon']['today_new'] = RestaurantService.get_today_coupon
    data['order']['today'] = RestaurantService.get_today_order
    data['shared']['today'] = RestaurantService.get_today_share

    return ops_render( "index.html",resp_data )



if __name__ == '__main__':
    # app.register_blueprint(route_index)

    app.run()
