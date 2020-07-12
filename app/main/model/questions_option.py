#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class QuestionsOption(db.Model):
    __tablename__ = 'tQuestionsOptions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questionId = db.Column(db.Integer, db.ForeignKey('tAbstractOptionableQuestions.id'), nullable=False)
    questionOptionId = db.Column(db.Integer, db.ForeignKey('tAbstractQuestionOptions.id'), nullable=False)


def main():
    pass


if __name__ == '__main__':
    main()
