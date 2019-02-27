# -*- coding: utf-8 -*-
"""Reset_request model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, BOOLEAN
from sqlalchemy.orm import relationship, backref
from uuid import uuid4
from datetime import datetime
from contacts.model import DeclarativeBase, metadata, DBSession
from tg import url, config
from registration import lib as mailer
from tg.i18n import ugettext as _

def get_token():
    return str(uuid4())

class ResetRequest(DeclarativeBase):
    __tablename__ = 'reset_requests'

    activated = Column(BOOLEAN, default=False)
    created = Column(DateTime, default=datetime.now)
    token = Column(
    	Unicode(255), 
    	unique=True, 
    	nullable=False,
    	default=get_token)
    uid = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('reset_requests',
                                        cascade='all, delete-orphan'))

    @classmethod
    def get_by_user(cls, user_id):
        return DBSession.query(ResetRequest)\
            .filter_by(user_id=user_id, activated=False).first()

    @classmethod
    def get_by_token(cls, token):
        return DBSession.query(ResetRequest)\
            .filter_by(token=token, activated=False).first()
    
    def check_token_age(self):
    	return abs(datetime.now() - self.created).days < 2

    def get_reset_url(self):
        return url('/reset_password/new_password',
                params=dict(token=self.token),
                qualified=True)

    def send_reset_link(self):
        email_address = self.user.email_address
        self.created = datetime.now()
        email_body = config.get(
            'reset_password.body',
            _('Please click on this link to reset your password') + '\n'\
                + self.get_reset_url() + '\n'\
                + _('The link is valid for 48 hours only')
        )
        email_data = {
            'sender': config['mail.default_sender'],
            'subject': _("Password reset request from %s") % 'site-name',
            'body': email_body,
            'rich': ''
        }
        try:
            mailer.send_email(email_address, **email_data)
        except Exception as ex:
            error_message = ''
            if hasattr(ex, 'message'):
                error_message = ex.message
            else:
                error_message = str(ex)
            return False, error_message
        return True, 'Mail sent to ' + self.user.email_address



__all__ = ['Reset_request']
