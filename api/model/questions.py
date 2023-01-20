from sqlalchemy.types import Text
from app import db


class QuestionsQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<User %r>' % self.name

    def to_dict(self):
        question_dict = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }
        return question_dict
