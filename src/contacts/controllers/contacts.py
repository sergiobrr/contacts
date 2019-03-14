from tgext.crud import EasyCrudRestController
from contacts.model import DBSession, Contact, User
from tg.predicates import not_anonymous
from tg import request, abort
from tg.decorators import with_trailing_slash, without_trailing_slash,\
	override_template
from tg import expose
from tgext.crud.decorators import optional_paginate, apply_default_filters
from sprox.formbase import AddRecordForm, EditableForm
from sprox.fillerbase import EditFormFiller, AddFormFiller 

__all__ = ['ContactController']

def get_user_id():
	user = request.identity.get('user', None)
	if user:
		return user.user_id
	else:
		abort(403, 'User non existent')


class ContactAddForm(AddRecordForm):
	__limit_fields__ = ['contact_name', 'contact_phonenumber', 'user']
	__model__ = Contact
	__omit_fields__ = ['id',]
	def _do_get_disabled_fields(self):
		'''
		disable the user field to ensure that
		it's not editable and it's the same as the current user
		'''
		return ['user', ]

contact_add_form = ContactAddForm(DBSession)


class ContactAddFormFiller(AddFormFiller):
	__model__ = Contact

	def get_value(self, values=None, **kw):
		user_id = get_user_id()
		_values = {
			'user': user_id, 
			'user_id': user_id
		}
		if values is None:
			values = {}
		values.update(_values)
		return super(ContactAddFormFiller, self).get_value(values, **kw)
contact_add_form_filler = ContactAddFormFiller(DBSession)


class ContactEditForm(EditableForm):
	__model__ = Contact
	__limit_fields__ = ['contact_name', 'contact_phonenumber']
contact_edit_form = ContactEditForm(DBSession)


class ContactController(EasyCrudRestController):
	# predicate that ensure the user is authenticated
	allow_only = not_anonymous()
	edit_form = contact_edit_form
	filters = {'user_id': lambda: request.identity['user'].user_id}
	model = Contact
	new_filler = contact_add_form_filler
	new_form = contact_add_form
	substring_filters = ['contact_name', 'contact_phonenumber']
	title = 'Contacts controller'

	# __table_options__ = {
	# 	'__omit_fields__': [
	# 		'id',
	# 		'user_id', 
	# 		'user'
	# 	]
	# }

	@expose( 'json')
	def put(self, *args, **kwargs):
		if kwargs and 'image' in kwargs.keys() and kwargs['image'] == '':
			kwargs['image'] = None 
		return super(ContactController, self).put(*args, **kwargs)

	@expose('contacts.templates.get_all', inherit=True)
	def get_all(self, *args, **kwargs):
		'''
		overrides the default template
		'''
		return super(ContactController, self).get_all(*args, **kwargs)

	@expose(inherit=True)
	def new(self, *args, **kwargs):
		'''
		it calls the filler get value to have
		the user field with the right value
		'''
		value = self.new_filler.get_value()
		return super(ContactController, self).new(
			user_id=value['user_id'],
			user=value['user'],
			**kwargs
		)

	@expose('json:')
	def json_data(self, *args, **kwargs):
		user_id = get_user_id()
		contacts = DBSession.query(Contact)\
				.filter(Contact.user_id == user_id).all()
		return dict(contacts=contacts)

