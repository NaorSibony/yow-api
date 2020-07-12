#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class MultiChoiceQuestionOption(db.Model):
    __tablename__ = 'tMultiChoiceQuestionOption'
    id = db.Column(db.Integer, db.ForeignKey('tAbstractQuestionOptions'), primary_key=True)
    explanation = db.Column(db.String(200))


def main():
    pass


if __name__ == '__main__':
    main()
