from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Text
from contacts.model import DeclarativeBase, metadata, DBSession


class Contact(DeclarativeBase):
	__tablename__ = 'contacts'

	id = Column(Integer, primary_key=True)
	contact_name = Column(Unicode(255), unique=True, nullable=False)
	contact_phonenumber = Column(Unicode(48), nullable=False)
	user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True, nullable=False)