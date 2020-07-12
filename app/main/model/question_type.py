#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class QuestionType(db.Model):
    __tablename__ = 'luQuestionTypes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    abstractQuestionsRef = db.relationship('AbstractQuestion', backref='questionType', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
