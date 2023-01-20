from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from api.model.questions import QuestionsQuestion


class QuestionsSchema(SQLAlchemySchema):

    class Meta:
        model = QuestionsQuestion
        load_instance = True

    id = auto_field()
    title = auto_field()


class QuestionsSchema2(SQLAlchemySchema):

    class Meta:
        model = QuestionsQuestion
        load_instance = True

    id = auto_field()
    title = auto_field()
    content = auto_field()
