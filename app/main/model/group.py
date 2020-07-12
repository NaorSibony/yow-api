#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from .. import db


class Group(db.Model):
    __tablename__ = 'tGroups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50))
    userId = db.Column(db.ForeignKey('tUsers.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    isDeleted = db.Column(db.Boolean, nullable=False, default=False)


def main():
    pass


if __name__ == '__main__':
    main()
#
#
# class foo{
#     id
#     className
#     iNeverChange
# List<fooDetails>
# }
#
# class fooDto{
# fooDetail
# }
#
#
# //one to many
#
# class fooDetails {
#     id
#     name
#     createdAt
#     fooId
#     isDeleted
# }

