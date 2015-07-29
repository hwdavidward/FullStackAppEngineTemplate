# -*- coding: utf-8 -*-
__author__ = 'DavidWard'

from flask.views import View


class Index(View):

    def dispatch_request(self):
        return "Welcome"


