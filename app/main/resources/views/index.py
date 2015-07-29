# -*- coding: utf-8 -*-
__author__ = 'DavidWard'

from flask.ext.restful import Resource


class Index(Resource):

    def get(self):
        print 'INDEX FOUND'
        return "Welcome"


