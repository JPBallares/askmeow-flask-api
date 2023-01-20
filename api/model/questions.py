from sqlalchemy.types import Text
from core.split import SplitSDK
from app import db

split = SplitSDK()


class QuestionsQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    treatment = split.get_treatment('*', 'question-content')

    if treatment == "on":
        content = db.Column(Text)

    def __init__(self, title, content):
        self.title = title

        treatment = split.get_treatment('*', 'question-content')
        if treatment == "on":
            self.content = content

    def __repr__(self):
        return '<User %r>' % self.name

    def to_dict(self):
        question_dict = {
            'id': self.id,
            'title': self.title,
        }

        treatment = split.get_treatment('*', 'question-content')
        if treatment == "on":
            question_dict['content'] = self.content
        return question_dict
