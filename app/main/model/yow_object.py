#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class YowObject(db.Model):
    __tablename__ = 'tYowObjects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    parentCategoryId = db.Column(db.Integer, db.ForeignKey('luObjectCategories.id'))
    objectTagsRef = db.relationship('ObjectTag', backref='yowObject', lazy=True)
    abstractQuestionOptionsRef = db.relationship('AbstractQuestionOption', backref='yowObject', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
