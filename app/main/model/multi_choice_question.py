#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class MultiChoiceQuestion(db.Model):
    __tablename__ = 'tMultiChoiceQuestions'
    id = db.Column(db.Integer, db.ForeignKey('tAbstractOptionableQuestions.id'), primary_key=True)
    imageId = db.Column(db.Integer, db.ForeignKey('tHostedImages.id'))
    correctOptionIndex = db.Column(db.Integer)


def main():
    pass


if __name__ == '__main__':
    main()
