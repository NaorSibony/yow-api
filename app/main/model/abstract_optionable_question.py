#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class AbstractOptionableQuestion(db.Model):
    __tablename__ = 'tAbstractOptionableQuestions'
    id = db.Column(db.Integer, db.ForeignKey('tAbstractQuestions.id'), primary_key=True)
    isShuffleAnswers = db.Column(db.Boolean, nullable=False)
    multiChoiceQuestionRef = db.relationship('MultiChoiceQuestion', backref='abstractOptionableQuestion',
                                             uselist=False, lazy=True)
    matchingQuestionRef = db.relationship('MatchingQuestion', backref='abstractOptionableQuestion',
                                          uselist=False, lazy=True)
    questionsOptionsRef = db.relationship('QuestionsOption', backref='abstractOptionableQuestion', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
