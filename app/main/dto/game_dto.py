#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restplus import Namespace, fields


class GameDto:
    api = Namespace('game', description='game related operations')
    game = api.model('Game', {
        'id': fields.Integer(required=False, description='game id'),
        'name': fields.String(required=True, description='game name'),
        'categoryId': fields.Integer(required=True, description='category id'),
        'themeId': fields.Integer(required=True, description='theme id'),
        'numOfQuestions': fields.Integer(required=False, description='number of questions in game'),
        'folderName': fields.String(required=False, description='name of containing folder')
    })


class AbstractGameQuestionDto:
    api = GameDto.api
    _abstract_game_question_fields = {
        'id': fields.Integer(required=False, description='abstract question id'),
        'name': fields.String(required=True, description='abstract question name'),
        'questionTypeId': fields.Integer(required=True, description='question type id')
    }
    abstract_game_question = api.model('AbstractGameQuestion', _abstract_game_question_fields)


class GameWithQuestionsDto:
    api = GameDto.api
    game_with_questions = api.model('GameWithQuestions', {
        'id': GameDto.game['id'],
        'name': GameDto.game['name'],
        'categoryId': GameDto.game['categoryId'],
        'themeId': GameDto.game['themeId'],
        'gameQuestions': fields.List(fields.Nested(AbstractGameQuestionDto.abstract_game_question), required=True,
                                     description='game questions'),
        'folderName': GameDto.game['folderName']
    })


class GameCategoryDto:
    api = GameDto.api
    game_category = api.model('GameCategory', {
        'id': fields.Integer(required=False, description='game category id'),
        'name': fields.String(required=True, description='game category name'),
        'themeIds': fields.List(fields.Integer, required=True, description='game category theme ids')
    })


class LookableDto:
    api = GameDto.api
    lookable = api.model('GameTheme', {
        'id': fields.Integer(required=False, description='theme id'),
        'name': fields.String(required=True, description='theme name')
    })


class AbstractQuestionOptionDto:
    api = GameDto.api
    _abstract_question_option_fields = {
        'id': fields.Integer(required=False, description='abstract question option id'),
        'name': fields.String(required=False, description='abstract question option name'),
        'objectId': fields.Integer(required=False, description='abstract question option object id')
    }
    abstract_question_option = api.model('AbstractQuestionOption', _abstract_question_option_fields)


class AbstractOptionsGameQuestionDto(AbstractGameQuestionDto):
    api = GameDto.api
    _abstract_options_game_question_fields = AbstractGameQuestionDto._abstract_game_question_fields.copy()
    _abstract_options_game_question_fields['options'] = fields.List(
        fields.Nested(AbstractQuestionOptionDto.abstract_question_option),
        required=True,
        description='abstract options game questions options'
    )
    abstract_options_game_question = api.model('AbstractOptionsGameQuestion', _abstract_options_game_question_fields)


class MultiChoiceQuestionOptionDto(AbstractQuestionOptionDto):
    api = GameDto.api
    multi_choice_question_option_fields = AbstractQuestionOptionDto._abstract_question_option_fields.copy()
    multi_choice_question_option_fields['explanation'] = fields.String(
        required=False,
        description='multi choice question option explanation'
    )
    multi_choice_question_option = api.model('MultiChoiceQuestionOption', multi_choice_question_option_fields)


class MultiChoiceGameQuestionDto(AbstractOptionsGameQuestionDto):
    api = GameDto.api
    multi_choice_game_question_fields = AbstractOptionsGameQuestionDto._abstract_options_game_question_fields.copy()
    multi_choice_game_question_fields['options'] = fields.List(
        fields.Nested(MultiChoiceQuestionOptionDto.multi_choice_question_option),
        required=True,
        description='multi choice game question options'
    )
    multi_choice_game_question = api.model('MultiChoiceGameQuestion', multi_choice_game_question_fields)


class MatchingQuestionOptionDto(AbstractQuestionOptionDto):
    api = GameDto.api
    _matching_question_option_fields = AbstractQuestionOptionDto._abstract_question_option_fields.copy()
    _matching_question_option_fields['label'] = fields.String(
        required=False,
        description='matching question option label'
    )
    matching_question_option = api.model('MatchingQuestionOption', _matching_question_option_fields)


class MatchingGameQuestionDto(AbstractOptionsGameQuestionDto):
    api = GameDto.api
    _matching_game_question_fields = AbstractOptionsGameQuestionDto._abstract_options_game_question_fields.copy()
    _matching_game_question_fields['options'] = fields.List(
        fields.Nested(MatchingQuestionOptionDto.matching_question_option),
        required=True,
        description='matching game question options'
    )
    _matching_game_question_fields['isShuffleAnswers'] = fields.Boolean(
        required=False,
        description='should matching game question shuffle answers?'
    )
    _matching_game_question_fields['minutes'] = fields.Integer(
        required=True,
        description='matching game question minutes'
    )
    _matching_game_question_fields['seconds'] = fields.Integer(
        required=True,
        description='matching game question seconds'
    )
    matching_game_question = api.model('MatchingGameQuestion', _matching_game_question_fields)


class HostedImageDto:
    api = GameDto.api
    hosted_image = api.model('HostedImage', {
        'id': fields.Integer(required=False, description='hosted image id'),
        'localName': fields.String(required=True, description='hosted image local name'),
        'url': fields.String(required=True, description='hosted image url')
    })


def main():
    pass


if __name__ == '__main__':
    main()
