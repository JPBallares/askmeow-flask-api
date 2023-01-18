from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from

from app import db
from api.model.questions import QuestionsQuestion
from api.schema.questions import QuestionsSchema


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
    return QuestionsSchema(many=True).dump(questions), 200
