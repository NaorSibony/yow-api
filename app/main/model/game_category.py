#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class GameCategory(db.Model):
    __tablename__ = 'luGameCategories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    gamesRef = db.relationship('Game', backref='gameCategory', lazy=True)
    gameCategoriesThemesRef = db.relationship('GameCategoriesTheme', backref='gameCategory', lazy=True)


def main():
    pass


if __name__ == '__main__':
    main()
