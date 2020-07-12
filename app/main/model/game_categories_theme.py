#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db


class GameCategoriesTheme(db.Model):
    __tablename__ = 'tGameCategoriesThemes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoryId = db.Column(db.Integer, db.ForeignKey('luGameCategories.id'), nullable=False)
    themeId = db.Column(db.Integer, db.ForeignKey('luGameThemes.id'), nullable=False)


def main():
    pass


if __name__ == '__main__':
    main()
