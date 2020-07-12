#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask_restplus import Resource
from ..dto.game_dto import GameDto, GameWithQuestionsDto, GameCategoryDto, LookableDto, AbstractGameQuestionDto
from ..service.game_service import add_new_question, create_new_game, delete_game, delete_question_from_game, \
    duplicate_game, get_all_games, get_game_by_id, get_all_game_categories, get_all_game_themes, update_game, \
    update_game_question

api = GameDto.api
_game = GameDto.game
_game_with_questions = GameWithQuestionsDto.game_with_questions
_game_category = GameCategoryDto.game_category
_lookable = LookableDto.lookable
_abstract_game_question = AbstractGameQuestionDto.abstract_game_question


@api.route('/')
class Game(Resource):
    @api.doc('Get all user\'s games')
    @api.marshal_list_with(_game)
    def get(self):
        """Get all users's games"""
        all_games = get_all_games()
        for game in all_games:
            game.numOfQuestions = len(game.gameQuestionsRef)
        return all_games

    @api.response(201, 'Game successfully created')
    @api.doc('Creates a new game')
    @api.expect(_game, validate=True)
    @api.marshal_with(_game)
    def post(self):
        """Creates a new game"""
        data = request.json
        return create_new_game(data=data)


@api.route('/<game_id>')
@api.param('game_id', 'Game identifier')
class GameById(Resource):
    @api.doc('Get game by id')
    @api.marshal_with(_game)
    def get(self, game_id):
        """Get game by id"""
        game = get_game_by_id(game_id)
        game.numOfQuestions = len(game.gameQuestionsRef)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            return game

    @api.doc('Update a game')
    @api.expect(_game)
    def put(self, game_id):
        """Update a game"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            data = request.json
            update_game(game, data)
            return {}

    @api.doc('Delete a game')
    def delete(self, game_id):
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            delete_game(game_id)
            return {}


@api.route('/<game_id>/detailed')
@api.param('game_id', 'Game identifier')
class Game(Resource):
    @api.doc('Get game by id with questions')
    @api.marshal_with(_game_with_questions)
    def get(self, game_id):
        """Get game by id with questions"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            game.gameQuestions = []
            for gq in game.gameQuestionsRef:
                game.gameQuestions.append(gq.abstractQuestion)
            return game


@api.route('/<game_id>/<question_id>')
@api.param('game_id', 'Game identifier')
@api.param('question_id', 'Question identifier')
class GameAndQuestionById(Resource):
    @api.doc('Remove question from game')
    def delete(self, game_id, question_id):
        """Remove question from game"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        elif int(question_id) not in [gq.id for gq in game.gameQuestionsRef]:
            api.abort(404, 'The provided question ID was not found in provided game')
        else:
            delete_question_from_game(game_id, question_id)
            return {}

    @api.doc('Update a question within a game')
    @api.marshal_with(_abstract_game_question)
    @api.expect(_abstract_game_question, validate=True)
    def put(self, game_id, question_id):
        """Update a question within a game"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        elif int(question_id) not in [gq.id for gq in game.gameQuestionsRef]:
            api.abort(404, 'The provided question ID was not found in provided game')
        else:
            data = request.json
            return update_game_question(game_id, question_id, data)


@api.route('/<game_id>/question')
@api.param('game_id', 'Game identifier')
class QuestionByGameId(Resource):
    @api.doc('Add new question to game')
    @api.expect(_abstract_game_question, validate=True)
    @api.marshal_with(_abstract_game_question)
    def post(self, game_id):
        """Add new question to game"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            data = request.json
            return add_new_question(game_id, data)


@api.route('/<game_id>/duplicate')
@api.param('game_id', 'Game identifier')
class DuplicateGame(Resource):
    @api.doc('Duplicate a game')
    @api.marshal_with(_game_with_questions)
    def post(self, game_id):
        """Duplicate a game"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            return duplicate_game(game), 201


@api.route('/<game_id>/flows')
@api.param('game_id', 'Game identifier')
class GameInFlow(Resource):
    @api.doc('Check if provided game exists in a flow')
    def get(self, game_id):
        """Check if provided game exists in a flow"""
        game = get_game_by_id(game_id)
        if not game:
            api.abort(404, 'Game not found.')
        else:
            if len(game.flowsGamesRef) > 0:
                return True
            else:
                return False


@api.route('/categories')
class GameCategoriesList(Resource):
    @api.doc('Lookup to get all the possible game categories (user for game creation)')
    @api.marshal_list_with(_game_category)
    def get(self):
        """Lookup to get all the possible game categories (user for game creation)"""
        all_game_categories = get_all_game_categories()
        for gc in all_game_categories:
            gc.themeIds = []
            for gct in gc.gameCategoriesThemesRef:
                gc.themeIds.append(gct.id)
        return all_game_categories


@api.route('/themes')
class LookableList(Resource):
    @api.doc('Lookup to get all the possible game themes (user for game creation)')
    @api.marshal_list_with(_lookable)
    def get(self):
        """Lookup to get all the possible game themes (user for game creation)"""
        return get_all_game_themes()


def main():
    pass


if __name__ == '__main__':
    main()
