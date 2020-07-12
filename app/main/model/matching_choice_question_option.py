#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class MatchingChoiceQuestionOption(db.Model):
    __tablename__ = 'tMatchingChoiceQuestionOption'
    id = db.Column(db.Integer, db.ForeignKey('tAbstractQuestionOptions'), primary_key=True)
    label = db.Column(db.String(30))


def main():
    pass


if __name__ == '__main__':
    main()
