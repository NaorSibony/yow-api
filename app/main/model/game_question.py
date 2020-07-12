#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class GameQuestion(db.Model):
    __tablename__ = 'tGameQuestions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gameId = db.Column(db.Integer, db.ForeignKey('tGames.id'), nullable=False)
    questionId = db.Column(db.Integer, db.ForeignKey('tAbstractQuestions.id'), nullable=False)


def main():
    pass


if __name__ == '__main__':
    main()
