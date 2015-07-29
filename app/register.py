# -*- coding: utf-8 -*-
__author__ = 'DavidWard'

import logging
import os
from flask import Flask


################
#### config ####
################
main_app = Flask('project_id_name', template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), "templates")))
logging.getLogger().setLevel(logging.INFO)


if os.getenv('FLASK_CONF') == 'DEV':
    main_app.config.from_object('app.settings.Development')
elif os.getenv('FLASK_CONF') == 'TEST':
    main_app.config.from_object('app.settings.Testing')
else:
    main_app.config.from_object('app.settings.Production')


####################
#### extensions ####
####################

# Enable jinja2 loop controls extension
main_app.jinja_env.add_extension('jinja2.ext.loopcontrols')


#############################
#### register blueprints ####
#############################

from app.main import main_blueprint
main_app.register_blueprint(main_blueprint)