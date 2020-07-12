#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from .. import db


class Game(db.Model):
    __tablename__ = 'tGames'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    folderName = db.Column(db.String(20))
    userId = db.Column(db.ForeignKey('tUsers.id'), nullable=False)
    categoryId = db.Column(db.Integer, db.ForeignKey('luGameCategories.id'), nullable=False)
    themeId = db.Column(db.Integer, db.ForeignKey('luGameThemes.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    gameQuestionsRef = db.relationship('GameQuestion', backref='game', lazy=True)
    flowsGamesRef = db.relationship('FlowsGame', backref='game', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
