from tgext.crud import EasyCrudRestController
from contacts.model import DBSession, Contact, User
from tg.predicates import not_anonymous
from tg import request
from tg.decorators import with_trailing_slash, without_trailing_slash
from tg import expose
from tgext.crud.decorators import optional_paginate, apply_default_filters
from sprox.formbase import AddRecordForm, EditableForm
from sprox.fillerbase import EditFormFiller, AddFormFiller


def get_user_id():
	identity = request.environ.get('repoze.who.identity')
	user = DBSession.query(User)\
			.filter(User.user_name == identity['repoze.who.userid']).one()
	return user.user_id


class ContactAddForm(AddRecordForm):
	__limit_fields__ = ['contact_name', 'contact_phonenumber', 'user']
	__model__ = Contact
	__omit_fields__ = ['id']

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


class ContactEditFormFiller(EditFormFiller):
	__model__ = Contact
contact_edit_form_filler = ContactEditFormFiller(DBSession)


class ContactEditForm(EditableForm):
	__model__ = Contact
	__limit_fields__ = ['contact_name', 'contact_phonenumber']
contact_edit_form = ContactEditForm(DBSession)


class ContactController(EasyCrudRestController):
	# predicate that ensure the user is authenticated
	allow_only = not_anonymous()
	edit_filler = contact_edit_form_filler
	edit_form = contact_edit_form
	model = Contact
	new_filler = contact_add_form_filler
	new_form = contact_add_form
	substring_filters = ['contact_name', 'contact_phonenumber']
	title = 'Contacts controller'

	__forms_options__ = {
		'__hide_fields__': [
			'id', 
			'user_id',
			'user'
		],
		'__field_order__': [
			'contact_name',
			'contact_phonenumber'
		]
	} 

	__table_options__ = {
		'__omit_fields__': [
			'id',
			'user_id', 
			'user'
		]
	}

	@with_trailing_slash
	@expose('genshi:contacts.templates.get_all')
	@expose('mako:contacts.templates.get_all')
	@expose('jinja:contacts.templates.get_all')
	@expose('kajiki:contacts.templates.get_all')
	@expose('json:')
	@optional_paginate('value_list')
	@apply_default_filters
	def get_all(self, *args, **kwargs):
		'''
		add a filter on user_id contact field in order to pass to
		view only contacts owned by the current user
		'''
		kwargs['user_id'] = get_user_id()
		return super(ContactController, self).get_all(*args, **kwargs)

	@without_trailing_slash
	@expose('genshi:tgext.crud.templates.new')
	@expose('mako:tgext.crud.templates.new')
	@expose('jinja:tgext.crud.templates.new')
	@expose('kajiki:tgext.crud.templates.new')
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

