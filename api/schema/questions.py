from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.model.questions import QuestionsQuestion


class QuestionsSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = QuestionsQuestion
        load_instance = True
