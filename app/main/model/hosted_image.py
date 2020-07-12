#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from .. import db


class HostedImage(db.Model):
    __tablename__ = 'tHostedImages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    localName = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    thumbnailUrl = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    multiChoiceQuestionRef = db.relationship('MultiChoiceQuestion', uselist=False, backref='hostedImage', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
