#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from .. import db


class Flow(db.Model):
    __tablename__ = 'tFlows'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(50))
    userId = db.Column(db.Integer, db.ForeignKey('tUsers.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    flowsGamesRef = db.relationship('FlowsGame', backref='flows', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
