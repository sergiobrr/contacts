from contacts.model.contact import Contact
from tg import expose, validate
from contacts.lib.base import BaseController
from contacts.model import DBSession
from tw2.forms import FileValidator
from tw2.core import IntValidator
from tgext.datahelpers.utils import fail_with
from PIL import Image
from io import BytesIO

class PhotoController(BaseController):

	@expose('json')
	@validate({
		'file': FileValidator(required=True),
		'contact_id': IntValidator(required=True)
	}, error_handler=fail_with(403))
	def save_image(self, file=None, contact_id=None):
		if contact_id and file:
			contact = DBSession.query(Contact).get(Contact.id == contact_id)
			if contact:
				contact.image = image
				return dict(message='image saved')
			else:
				return dict(message='bad contact')
		else:
			return dict(message='missing file or id')
				

