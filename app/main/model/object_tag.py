#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class ObjectTag(db.Model):
    __tablename__ = 'tObjectTags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    objectId = db.Column(db.Integer, db.ForeignKey('tYowObjects.id'), nullable=False)
    hashTagId = db.Column(db.Integer, db.ForeignKey('vHashTags.id'), nullable=False)


def main():
    pass


if __name__ == '__main__':
    main()
