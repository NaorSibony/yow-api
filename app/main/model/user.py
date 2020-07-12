#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db


class User(db.Model):
    __tablename__ = 'tUsers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    gamesRef = db.relationship('Game', backref='user', lazy=True)
    groupsRef = db.relationship('Group', backref='user', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
