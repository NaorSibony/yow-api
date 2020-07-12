#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class GameTheme(db.Model):
    __tablename__ = 'luGameThemes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    gameCategoriesThemesRef = db.relationship('GameCategoriesTheme', backref='gameTheme', lazy=True)
    gamesRef = db.relationship('Game', backref='gameTheme', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
