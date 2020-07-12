#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from app.main import db
from app.main.model.abstract_question import AbstractQuestion
from app.main.model.game import Game
from app.main.model.game_category import GameCategory
from app.main.model.game_theme import GameTheme
from app.main.model.game_question import GameQuestion
from app.main.model.flows_game import FlowsGame


def add_new_question(game_id, data):
    abstract_question = AbstractQuestion(name=data['name'], questionTypeId=data['questionTypeId'])
    save_to_db(abstract_question)
    game_question = GameQuestion(gameId=game_id, questionId=abstract_question.id)
    save_to_db(game_question)
    return abstract_question, 201


def create_new_game(data):
    # TODO need to remember to implement the user id pulling
    user_id = 1
    new_game = Game(
        name=data['name'],
        userId=user_id,
        categoryId=data['categoryId'],
        themeId=data['themeId']
    )
    save_to_db(new_game)
    return new_game, 201


def delete_game(game_id):
    Game.query.filter_by(id=game_id).delete()
    db.session.commit()


def delete_question_from_game(game_id, question_id):
    GameQuestion.query.filter_by(id=question_id, gameId=game_id).delete()
    # TODO should we also delete the question from tAbstractQuestions? I'm guessing no, because of the 1:many relation
    db.session.commit()


def duplicate_game(game):
    # Duplicate the game object
    game_dup = Game(
        name=game.name,
        userId=game.userId,
        categoryId=game.categoryId,
        themeId=game.themeId
    )
    save_to_db(game_dup)

    # Duplicate the game Questions reference
    for gq in game.gameQuestionsRef:
        save_to_db(GameQuestion(gameId=game_dup.id, questionId=gq.questionId))

    # Duplicate the flows games reference
    for gf in game.flowsGamesRef:
        save_to_db(FlowsGame(gameId=game_dup.id, flowId=gf.flowId, order=gf.order))

    # Add game questions to the duplicate game object which will be returned
    game_dup.gameQuestions = []
    for gq in game_dup.gameQuestionsRef:
        game_dup.gameQuestions.append(gq.abstractQuestion)
    return game_dup


def get_all_games():
    return Game.query.all()


def get_game_by_id(game_id):
    return Game.query.filter_by(id=game_id).first()


def get_all_game_categories():
    return GameCategory.query.all()


def get_all_game_themes():
    return GameTheme.query.all()


def update_game(game, data):
    for field in ['name', 'categoryId', 'themeId']:
        if data.get(field):
            setattr(game, field, data[field])
    game.updatedAt = datetime.utcnow()
    save_to_db(game)


def update_game_question(game_id, question_id, data):
    game_question = GameQuestion.query.filter_by(id=question_id, gameId=game_id).first()
    abstract_question = AbstractQuestion.query.filter_by(id=game_question.questionId).first()
    for field in ['name', 'questionTypeId']:
        if data.get(field):
            setattr(abstract_question, field, data[field])
    abstract_question.updatedAt = datetime.utcnow()
    save_to_db(abstract_question)
    return abstract_question


def save_to_db(data):
    db.session.add(data)
    db.session.commit()


def main():
    pass


if __name__ == '__main__':
    main()
