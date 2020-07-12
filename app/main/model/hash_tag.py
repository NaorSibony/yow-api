#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class HashTag(db.Model):
    __tablename__ = 'vHashTags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    occurrences = db.Column(db.Integer, nullable=False)
    objectTagsRef = db.relationship('ObjectTag', backref='hashTags', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
