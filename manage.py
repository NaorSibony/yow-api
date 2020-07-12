#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app import blueprint
from app.main.util.db_ops import DbSeed

app = create_app(os.getenv('YOW_ENV', 'dev'))
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

db_seeder = DbSeed(db)


@manager.command
def run():
    # TODO stop listening on the public interface once we've implemented gunicorn
    app.run(host='0.0.0.0')


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def db_drop():
    db.drop_all()
    print('Database Dropped!')


@manager.command
def db_create():
    db.create_all()
    print('Database Created!')


@manager.command
def db_recreate():
    db_drop()
    db_create()
    db_seeder.seed()
    print('Database seeded!')


if __name__ == '__main__':
    manager.run()
