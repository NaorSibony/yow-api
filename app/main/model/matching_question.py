#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class MatchingQuestion(db.Model):
    __tablename__ = 'tMatchingQuestions'
    id = db.Column(db.Integer, db.ForeignKey('tAbstractOptionableQuestions.id'), primary_key=True)
    minutes = db.Column(db.Integer, nullable=False)
    seconds = db.Column(db.Integer, nullable=False)


def main():
    pass


if __name__ == '__main__':
    main()
