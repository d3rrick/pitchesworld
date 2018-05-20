import unittest
from flask_testing import TestCase
from app import bcrypt
from app import db
from app.models import *
from datetime import datetime
from app.auth.forms import RegistrationForm,LoginForm

class TestUser(unittest.TestCase):
	global user

	def setUp(self):
		self.hashed_password = bcrypt.generate_password_hash('secrets').decode("utf-8")
		self.user_derrick = User(username="derrick",password_hash=self.hashed_password,email="derrick@gmail.com",joined=datetime.utcnow(),profile_pic_path="/path/to/picture")
		
		# User.query.delete()
		

	def test_check_instance_variables(self):
		self.assertEquals(self.user_derrick.username,'derrick')
		self.assertEquals(self.user_derrick.email, 'derrick@gmail.com')


	def test_harshing(self):
		self.assertTrue(bcrypt.check_password_hash(self.user_derrick.password_hash, 'secrets'))

	def test_save_user(self):
		# db.session.add(self.user_derrick)
		# db.session.commit()
		self.assertTrue(len(User.query.all())>0)

	def test_whether_data_is_saved(self):
		# db.session.add(self.user_derrick)
		# db.session.commit()
		user = User.query.filter_by(username=self.user_derrick.username).first()
		self.assertEquals(self.user_derrick.username,user.username)

	

class TestPitch(unittest.TestCase):

	def setUp(self):
		self.pitch = Pitch(body="cool friday",author_id=33,upvotes=10, downvotes=5,category='promotion',timestamp=datetime.utcnow())

	def tearDown(self):
		pass

		# Pitch.query.delete()

	def test_check_pitch_instance_variables(self):
		self.assertEquals(self.pitch.body,"cool friday")
		self.assertEquals(self.pitch.downvotes, 5)

	def test_save_pitch(self):
		# db.session.add(self.pitch)
	
		db.session.commit()
		self.assertTrue(len(Pitch.query.all())>0)

	def test_whether_pitch_data_is_saved(self):
		# db.session.add(self.pitch)
		# db.session.commit()
		pitch = Pitch.query.filter_by(category=self.pitch.category).first()
		self.assertEquals(self.pitch.category,pitch.category)

class TestComment(unittest.TestCase):

	def setUp(self):
		self.comment = Comment(author_id=33,pitch_id=25,body="nyce one",timestamp=datetime.utcnow())

	def tearDown(self):
		Comment.query.delete()

	def test_check_comment_instance_variables(self):
		self.assertEquals(self.comment.body,"nyce one")
		self.assertEquals(self.comment.author_id, 33)

	def test_save_comment(self):
		db.session.add(self.comment)
		db.session.commit()
		self.assertTrue(len(Comment.query.all())>0)

	def test_whether_comment_data_is_saved(self):
		db.session.add(self.comment)
		db.session.commit()
		comment = Comment.query.filter_by(author_id=self.comment.author_id).first()
		self.assertEquals(self.comment.author_id,comment.author_id)


class TestRegistrationForm(unittest.TestCase):
	def setUp(self):
		self.new_form = RegistrationForm(email="admin@gmail.com",username="Admin",password="secret",password_confirm="secret")


	def test_registration(self):
		# print(self.new_form.data)

		self.assertEquals(self.new_form.data['username'],'Admin')
		self.assertEquals(self.new_form.data['submit'],False)

class TestLoginForm(unittest.TestCase):
	def setUp(self):
		self.new_form = LoginForm(email="admin@gmail.com",password="secret",remember=True)


	def test_login_form(self):

		self.assertEquals(self.new_form.data['email'],'admin@gmail.com')
		self.assertEquals(self.new_form.data['password'],"secret")
		self.assertEquals(self.new_form.data['remember'],True)