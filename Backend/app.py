# -*- coding: utf-8 -*-
from Backend import create_app
from Backend.libs.UrlManager import UrlManager

if __name__ == '__main__':
    app = create_app()
    app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
    app.add_template_global(UrlManager.buildUrl, 'buildUrl')
    app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')
    app.run()
