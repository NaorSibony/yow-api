#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.main.model import abstract_optionable_question, abstract_question, abstract_question_option, flow, \
    flows_game, game, game_categories_theme, game_category, game_question, game_theme, group, hash_tag, hosted_image, \
    matching_choice_question_option, matching_question, multi_choice_question, multi_choice_question_option, \
    object_category, object_tag, question_type, questions_option, user, yow_object


class DbSeed:
    def __init__(self, db):
        self.db = db

    def seed(self):
        print('Seeding Abstract Questions..')
        self.__seed_abstract_questions()
        print('Done')
        print('Seeding Abstract Optionable Questions..')
        self.__seed_abstract_optionable_questions()
        print('Done')
        print('Seeding Abstract Question Options..')
        self.__seed_abstract_question_options()
        print('Done')
        print('Seeding Flows..')
        self.__seed_flows()
        print('Done')
        print('Seeding Flows Games..')
        self.__seed_flows_games()
        print('Done')
        print('Seeding Games..')
        self.__seed_games()
        print('Done')
        print('Seeding Game Categories Themes..')
        self.__seed_game_categories_themes()
        print('Done')
        print('Seeding Game Categories..')
        self.__seed_game_categories()
        print('Done')
        print('Seeding Game Questions..')
        self.__seed_game_questions()
        print('Done')
        print('Seeding Game Themes..')
        self.__seed_game_themes()
        print('Done')
        print('Seeding Hash Tags..')
        self.__seed_hash_tags()
        print('Done')
        print('Seeding Hosted Images..')
        self.__seed_hosted_image()
        print('Done')
        print('Seeding Matching Choice Question Options..')
        self.__seed_matching_choice_question_options()
        print('Done')
        print('Seeding Matching Questions..')
        self.__seed_matching_questions()
        print('Done')
        print('Seeding Multi Choice Question Options..')
        self.__seed_multi_choice_question_options()
        print('Done')
        print('Seeding Multi Choice Questions..')
        self.__seed_multi_choice_questions()
        print('Done')
        print('Seeding Object Categories..')
        self.__seed_object_categories()
        print('Done')
        print('Seeding Object Tags..')
        self.__seed_object_tags()
        print('Done')
        print('Seeding Question Types..')
        self.__seed_question_types()
        print('Done')
        print('Seeding Questions Options..')
        self.__seed_questions_options()
        print('Done')
        print('Seeding Users..')
        self.__seed_users()
        print('Done')
        print('Seeding Yow Objects..')
        self.__seed_yow_objects()
        self.db.session.commit()

    def __seed_abstract_optionable_questions(self):
        self.db.session.add(abstract_optionable_question.AbstractOptionableQuestion(id=1, isShuffleAnswers=True))
        self.db.session.add(abstract_optionable_question.AbstractOptionableQuestion(id=2, isShuffleAnswers=False))
        self.db.session.commit()

    def __seed_abstract_questions(self):
        self.db.session.add(abstract_question.AbstractQuestion(id=1, name='AbstractQuestion1', questionTypeId=1))
        self.db.session.add(abstract_question.AbstractQuestion(id=2, name='AbstractQuestion2', questionTypeId=2))
        self.db.session.commit()

    def __seed_abstract_question_options(self):
        self.db.session.add(abstract_question_option.AbstractQuestionOption(objectId=1, name='AbstractQuestionOption1'))
        self.db.session.add(abstract_question_option.AbstractQuestionOption(objectId=2, name='AbstractQuestionOption2'))
        self.db.session.add(abstract_question_option.AbstractQuestionOption(objectId=3, name='AbstractQuestionOption3'))
        self.db.session.commit()

    def __seed_game_categories(self):
        self.db.session.add(game_category.GameCategory(name='GameCategory1'))
        self.db.session.add(game_category.GameCategory(name='GameCategory2'))
        self.db.session.commit()

    def __seed_game_categories_themes(self):
        self.db.session.add(game_categories_theme.GameCategoriesTheme(categoryId=1, themeId=1))
        self.db.session.add(game_categories_theme.GameCategoriesTheme(categoryId=1, themeId=2))
        self.db.session.add(game_categories_theme.GameCategoriesTheme(categoryId=1, themeId=3))
        self.db.session.add(game_categories_theme.GameCategoriesTheme(categoryId=2, themeId=4))
        self.db.session.commit()

    def __seed_game_questions(self):
        self.db.session.add(game_question.GameQuestion(gameId=1, questionId=1))
        self.db.session.add(game_question.GameQuestion(gameId=1, questionId=2))
        self.db.session.add(game_question.GameQuestion(gameId=2, questionId=1))
        self.db.session.commit()

    def __seed_game_themes(self):
        self.db.session.add(game_theme.GameTheme(name='GameTheme1'))
        self.db.session.add(game_theme.GameTheme(name='GameTheme2'))
        self.db.session.add(game_theme.GameTheme(name='GameTheme3'))
        self.db.session.add(game_theme.GameTheme(name='GameTheme4'))
        self.db.session.commit()

    def __seed_games(self):
        self.db.session.add(game.Game(name='Game1', folderName='Folder1', userId=1, categoryId=1, themeId=1))
        self.db.session.add(game.Game(name='Game2', userId=2, categoryId=2, themeId=2))
        self.db.session.commit()
    
    def __seed_flows(self):
        self.db.session.add(flow.Flow(name='Flow1', description='My flow', userId=1))
        self.db.session.add(flow.Flow(name='Flow2', userId=1))
        self.db.session.commit()
    
    def __seed_flows_games(self):
        self.db.session.add(flows_game.FlowsGame(gameId=1, flowId=1, order=1))
        self.db.session.add(flows_game.FlowsGame(gameId=1, flowId=1, order=2))
        self.db.session.add(flows_game.FlowsGame(gameId=1, flowId=2, order=1))
        self.db.session.commit()
    
    def __seed_hash_tags(self):
        self.db.session.add(hash_tag.HashTag(name='HashTag1', occurrences=5))
        self.db.session.add(hash_tag.HashTag(name='HashTag2', occurrences=7))
        self.db.session.add(hash_tag.HashTag(name='HashTag3', occurrences=2))
        self.db.session.commit()

    def __seed_hosted_image(self):
        self.db.session.add(
            hosted_image.HostedImage(
                localName='HostedImage1',
                url='https://fake-url.com/hostedImage1',
                thumbnailUrl='https://fake-url.com/hostedImage1Thumbnail'
            )
        )
        self.db.session.add(
            hosted_image.HostedImage(
                localName='HostedImage2',
                url='https://fake-url.com/hostedImage2',
                thumbnailUrl='https://fake-url.com/hostedImage2Thumbnail'
            )
        )
        self.db.session.commit()

    def __seed_matching_choice_question_options(self):
        self.db.session.add(
            matching_choice_question_option.MatchingChoiceQuestionOption(
                id=1,
                label='MatchingChoiceQuestionOption1'
            )
        )
        self.db.session.add(
            matching_choice_question_option.MatchingChoiceQuestionOption(
                id=2,
                label='MatchingChoiceQuestionOption2'
            )
        )
        self.db.session.commit()

    def __seed_matching_questions(self):
        self.db.session.add(matching_question.MatchingQuestion(id=1, minutes=10, seconds=2))
        self.db.session.add(matching_question.MatchingQuestion(id=2, minutes=5, seconds=34))
        self.db.session.commit()

    def __seed_multi_choice_question_options(self):
        self.db.session.add(
            multi_choice_question_option.MultiChoiceQuestionOption(
                id=1,
                explanation='Multi Choice Question Option 1'
            )
        )
        self.db.session.add(
            multi_choice_question_option.MultiChoiceQuestionOption(
                id=2,
                explanation='Multi Choice Question Option 2'
            )
        )
        self.db.session.commit()

    def __seed_multi_choice_questions(self):
        self.db.session.add(multi_choice_question.MultiChoiceQuestion(id=1, imageId=1))
        self.db.session.add(multi_choice_question.MultiChoiceQuestion(id=2, correctOptionIndex=1))
        self.db.session.commit()

    def __seed_object_categories(self):
        self.db.session.add(object_category.ObjectCategory(name='ObjectCategory1'))
        self.db.session.add(object_category.ObjectCategory(name='ObjectCategory2'))
        self.db.session.add(object_category.ObjectCategory(name='ObjectCategory3'))
        self.db.session.commit()

    def __seed_object_tags(self):
        self.db.session.add(object_tag.ObjectTag(objectId=1, hashTagId=1))
        self.db.session.add(object_tag.ObjectTag(objectId=2, hashTagId=2))
        self.db.session.commit()

    def __seed_question_types(self):
        self.db.session.add(question_type.QuestionType(name='QuestionType1'))
        self.db.session.add(question_type.QuestionType(name='QuestionType2'))
        self.db.session.commit()

    def __seed_questions_options(self):
        self.db.session.add(questions_option.QuestionsOption(questionId=1, questionOptionId=1))
        self.db.session.add(questions_option.QuestionsOption(questionId=2, questionOptionId=2))
        self.db.session.commit()

    def __seed_users(self):
        self.db.session.add(user.User(email='user1@foo.com'))
        self.db.session.add(user.User(email='user2@bar.com'))
        self.db.session.commit()

    def __seed_yow_objects(self):
        self.db.session.add(yow_object.YowObject(name='YowObject1', parentCategoryId=1))
        self.db.session.add(yow_object.YowObject(name='YowObject2', parentCategoryId=2))
        self.db.session.commit()


def main():
    pass


if __name__ == '__main__':
    main()
