from tgext.crud import EasyCrudRestController
from markupsafe import Markup
from contacts.model import DBSession, Contact, User
from tg.predicates import not_anonymous
from tg import request, abort
from tg.decorators import with_trailing_slash, without_trailing_slash,\
	override_template
from tg import expose
from tgext.crud.decorators import optional_paginate, apply_default_filters
from sprox.formbase import AddRecordForm, EditableForm
from sprox.fillerbase import EditFormFiller, AddFormFiller 
from tg.i18n import lazy_ugettext as l_
import kajiki

__all__ = ['ContactController']

def get_user_id():
	user = request.identity.get('user', None)
	if user:
		return user.user_id
	else:
		abort(403, 'User non existent')


class ContactController(EasyCrudRestController):
	# predicate that ensure the user is authenticated
	allow_only = not_anonymous()
	filters = {'user_id': lambda: request.identity['user'].user_id}
	json_dictify = False
	model = Contact
	substring_filters = ['contact_name', 'contact_phonenumber']
	title = 'Contacts controller'

	__form_edit_options__ = {
		"__limit_fields__": ['contact_name', 'contact_phonenumber']
	}

	__form_new_options__ = {
		"__hide_fields__": ['user', ],
		"__limit_fields__": ['contact_name', 'contact_phonenumber', 'user']
	}

	def _actions(filler, row):
		template = '''
		<div>
			<a href="${id}/edit" class="btn btn-primary">
		        <span class="glyphicon glyphicon-pencil"></span>
		    </a>
		    <div class="hidden-lg hidden-md">&nbsp;</div>
		    <form method="POST" action="${id}" style="display: inline">
		        <input type="hidden" name="_method" value="DELETE" />
		        <button type="submit" class="btn btn-danger" onclick="return confirm('${msg}')">
		            <span class="glyphicon glyphicon-trash"></span>
		        </button>
		    </form>
			<py:if test="image == None">
				<button class="btn btn-primary" 
	                ngf-select="vm.upload($$files, ${id})"
	                ngf-multiple="false">
	                <span class="glyphicon glyphicon-plus"></span>
	            </button>
			</py:if><py:else>
				<button class="btn btn-primary" 
	                ngf-select="vm.upload($$files, ${id})"
	                ngf-multiple="false">
	                <span class="glyphicon glyphicon-edit"></span>
	            </button>
	            <button class="btn btn-danger" 
	                ng-click="vm.delete(${id})">
	                <span class="glyphicon glyphicon-trash"></span>
	            </button>
			</py:else>
		</div>
		'''
		Template = kajiki.XMLTemplate(template)
		return Template(dict(
			id=row.id, 
			image=row.image, 
			msg=l_('Are you sure?'))).render()

	__table_options__ = {
	    '__omit_fields__': ['id', 'user_id', 'user'],
		'__xml_fields__': ['image'],
		'image': lambda filler, row: '<img src="%s" style="max-height:100px;" />' % row.image.thumb_url if row.image else '',		
		'__actions__': _actions
	}

	@expose( 'json')
	def put(self, *args, **kwargs):
		if kwargs and 'image' in kwargs.keys() and kwargs['image'] == '':
			kwargs['image'] = None 
		return super(ContactController, self).put(*args, **kwargs)

	@expose(inherit=True)
	def new(self, *args, **kwargs):
		'''
		it calls the filler get value to have
		the user field with the right value
		'''
		return super(ContactController, self).new(
			user_id=get_user_id(),
			user=get_user_id(),
			**kwargs
		)

	@expose('json:')
	def json_data(self, *args, **kwargs):
		user_id = get_user_id()
		contacts = DBSession.query(Contact)\
				.filter(Contact.user_id == user_id).all()
		return dict(contacts=contacts)

