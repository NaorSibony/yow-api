#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class AbstractQuestionOption(db.Model):
    __tablename__ = 'tAbstractQuestionOptions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    objectId = db.Column(db.Integer, db.ForeignKey('tYowObjects.id'))
    name = db.Column(db.String(30), nullable=False)
    matchingChoiceQuestionOptionRef = db.relationship('MatchingChoiceQuestionOption', uselist=False,
                                                      backref='abstractQuestionOption', lazy=True)
    multiChoiceQuestionOptionRef = db.relationship('MultiChoiceQuestionOption', uselist=False,
                                                   backref='abstractQuestionOption', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
