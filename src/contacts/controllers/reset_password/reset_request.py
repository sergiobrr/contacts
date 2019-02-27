# -*- coding: utf-8 -*-
"""Reset_request controller module"""

from tg import expose, redirect, validate, flash, url
from tg.i18n import ugettext as _
from tg.predicates import is_anonymous

from contacts.lib.base import BaseController
from contacts.model import DBSession
from contacts.model.auth import User
from contacts.model.reset_password.reset_request import ResetRequest


class ResetRequestController(BaseController):
    # Uncomment this line if your controller requires an authenticated user
    allow_only = is_anonymous()

    @expose('contacts.templates.reset_password.new_password')
    def new_password(self, token):
        request = ResetRequest.get_by_token(token)
        if request is None or request.check_token_age == False:
            if request is not None:
                DBSession.delete(request)
                DBSession.commit()
            redirect('/reset_password/bad_token')

        return dict(
            page='new_password', 
            token=token,
            user=request.user.email_address
        )

    @expose('contacts.templates.reset_password.bad_token')
    def bad_token(self):
        return dict(page='bad_token')
    
    @expose('contacts.templates.reset_password.reset_password')
    def reset_request(
        self, 
        failure=None,
        email_address=None,
        error_message=None
    ):
        '''
        Start the reset password procedure
        '''
        if failure is not None:
            if failure == 'user-not-found':
                flash(_("We don't have a user with %s as email address.") % email_address, 'error')
            if failure == 'request-already-present':
                flash(_("A reset request for %s was already present. We sent the email again, check your inbox") % email_address, 'info')
            if failure == 'email-error':
                flash_string = _("Error sending the reset request, try again later.")
                if error_message is not None:
                    flash_string += _("The error was %s") & error_message
                flash(flash_string, 'error')
        if failure is None and email_address is not None: 
            flash(_("A message with the link for the reset was sent to %s.") % email_address, 'info')
        return dict(
            page='reset_password',
            email_address=email_address
        )

    @expose()
    def reset_submission(self, email_address):
        '''
        Manage password reset submission
        '''
        user = User.by_email_address(email_address)
        if not user:
            redirect(
                '/reset_password/reset_request/?failure=user-not-found&email_address=' + email_address
            )
        request = ResetRequest.get_by_user(user.user_id)
        already_present = False
        result = False
        message = ''
        if request:
            already_present = True
            result, message = request.send_reset_link()
        else:
            request = ResetRequest(user_id=user.user_id)
            DBSession.add(request)
            DBSession.flush()
            request = ResetRequest.get_by_user(user.user_id)
            result, message = request.send_reset_link()

        if result:
            if already_present:
                redirect(
                    '/reset_password/reset_request/?failure=request-already-present&email_address=' + email_address
                )
            else:
                redirect('/reset_password/reset_request/?email_address=' + email_address)
        else:
            redirect(
                    '/reset_password/reset_request/?failure=email-error&error_message=' + message)
