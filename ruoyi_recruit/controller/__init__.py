# -*- coding: utf-8 -*-
# @Module: ruoyi_recruit/controller

from flask import Blueprint

recruit_info = Blueprint('recruit_info', __name__, url_prefix='/recruit/recruit')


from . import recruit_info_controller
