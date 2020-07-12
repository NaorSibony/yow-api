#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restplus import Api
from flask import Blueprint

from .main.controller.game_controller import api as game_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='YOW API',
          version='1.0',
          description='YOW RESTful API Service'
          )

api.add_namespace(game_ns, path='/games')


def main():
    pass


if __name__ == '__main__':
    main()
