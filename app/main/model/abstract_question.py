#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from .. import db


class AbstractQuestion(db.Model):
    __tablename__ = 'tAbstractQuestions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    questionTypeId = db.Column(db.Integer, db.ForeignKey('luQuestionTypes.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    gameQuestionsRef = db.relationship('GameQuestion', backref='abstractQuestion', lazy=True)
    abstractOptionableQuestionRef = db.relationship('AbstractOptionableQuestion', backref='abstract_question',
                                                    uselist=False, lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
