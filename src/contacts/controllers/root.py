# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from contacts import model
from contacts.controllers.secure import SecureController
from contacts.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.tgadminconfig import CrudRestControllerConfig
from tgext.admin.controller import AdminController
from tg.decorators import with_trailing_slash

from contacts.lib.base import BaseController
from contacts.controllers.error import ErrorController
from contacts.controllers.contacts import ContactController
from contacts.controllers.reset_password.reset_request import ResetRequestController
from tw2.core import CSSSource, JSSource, CSSLink, JSLink
from tgext.crud.resources import crud_script, crud_style
from copy import deepcopy

__all__ = ['RootController']

def get_layout():
    crud_resources = [
        crud_style,
        crud_script,
        CSSLink(
            location='head', 
            link='https://cdnjs.cloudflare.com/ajax/libs/angularjs-toaster/3.0.0/toaster.min.css'
        ),
        JSLink(
            location='headbottom',
            link='https://ajax.googleapis.com/ajax/libs/angularjs/1.7.7/angular.min.js'
        ),
        JSLink(
            location='headbottom',
            link='https://cdn.jsdelivr.net/npm/angular-animate@1.7.7/angular-animate.min.js'
        ),
        JSLink(
            location='headbottom',
            link='/javascript/app/ng-file-upload-shim.min.js'
        ),
        JSLink(
            location='headbottom',
            link='/javascript/app/ng-file-upload.min.js'
        ),
        JSLink(
            location='headbottom',
            link='https://cdnjs.cloudflare.com/ajax/libs/angularjs-toaster/3.0.0/toaster.min.js'
        ),
        JSLink(
            location='headbottom',
            link='/javascript/app/app.js'
        ),
        JSLink(
            location='headbottom',
            link='/javascript/app/photolist-controller.js'
        )
    ]
    layout = deepcopy(TGAdminConfig.layout)
    layout.crud_resources = crud_resources
    return layout


class CustomCrudConfig(CrudRestControllerConfig):
    defaultCrudRestController = ContactController
    layout = get_layout()


class RootController(BaseController):
    """
    The root controller for the contacts application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    # Added ContactController for the /contacts route
    contacts = AdminController.make_controller(CustomCrudConfig(ContactController.model), DBSession)
    # Added ResetPasswordController
    reset_password = ResetRequestController()

    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "contacts"

    @expose('contacts.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('contacts.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('contacts.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """Start the user login."""
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)
        