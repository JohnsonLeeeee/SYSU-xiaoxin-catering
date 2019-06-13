# -*- coding: utf-8 -*-

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        # release_version = app.config.get( 'RELEASE_VERSION' )
        # ver = "%s"%( int( time.time() ) ) if not release_version else release_version
        path =  "/static" + path
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildImageUrl( path ):
        url = "Image/" + path
        return url