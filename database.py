from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_name = sa.Column(sa.Text, nullable=False)
    group_id = sa.orm.relationship('Group')

class Group(Base):
    __tablename__ = 'group'

    group_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    group_name = sa.Column(sa.Text, nullable=False)

class Subjects(Base):
    __tablename__ = 'subjects'

    sub_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    sub_name = sa.Column(sa.Text, nullable=False)
