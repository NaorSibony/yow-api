#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .. import db


class FlowsGame(db.Model):
    __tablename__ = 'tFlowsGames'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gameId = db.Column(db.Integer, db.ForeignKey('tGames.id'), nullable=False)
    flowId = db.Column(db.Integer, db.ForeignKey('tFlows.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)


def main():
    pass


if __name__ == '__main__':
    main()
