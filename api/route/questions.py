from http import HTTPStatus
from flask import Blueprint, jsonify
from flasgger import swag_from

from app import db
from core.split import SplitSDK

from api.model.questions import QuestionsQuestion
from api.schema.questions import QuestionsSchema, QuestionsSchema2

split = SplitSDK()

questions_api = Blueprint('questions_api', __name__)


@questions_api.route('/questions')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'schema': QuestionsSchema
        },
    }
})
def questions():
    """
    Returns list of all questions
    ---
    """
    questions = db.session.execute(db.select(QuestionsQuestion)).scalars()
    treatment = split.get_treatment('*', 'show_tags')
    schemas = {
        'on': QuestionsSchema2,
        'off': QuestionsSchema,
    }
    return schemas[treatment](many=True).dump(questions), 200
