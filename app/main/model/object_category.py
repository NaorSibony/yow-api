#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class ObjectCategory(db.Model):
    __tablename__ = 'luObjectCategories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    yowObjectsRef = db.relationship('YowObject', backref='objectCategories', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
