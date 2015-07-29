# -*- coding: utf-8 -*-
__author__ = 'DavidWard'

from flask import Blueprint


################
#### config ####
################

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='templates',
    url_prefix='/'
)

################
#### routes ####
################

#  Home Page
from app.main.resources.views.index import Index
main_blueprint.add_url_rule('/', view_func=Index.as_view('index'))
