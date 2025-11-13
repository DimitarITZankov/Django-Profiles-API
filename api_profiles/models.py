from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager #BaseUserManager is needed for custom manager logic

class UserProfileManager(BaseUserManager):
	def create_user(self,username,name,email,password=None):
		if not username:
			raise ValueError("Every user must have a username")
		if not email:
			raise ValueError("Every user must have an email")
		email = self.normalize_email(email) #Standartize the email first part case-sensitive, after the @ non-sensitive
		user = self.model(username=username,name=name,email=email)

		user.set_password(password) #Hashes the password with the built-in hashing system in Django
		user.save(using=self._db)
		return user

	def create_superuser(self,username,name,email,password):
		user = self.create_user(username,name,password)
		user.is_superuser = True
		user.is_staff = True 
		user.save(using=self._db)
		return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
	username = models.CharField(max_length=30)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	is_active = models.BooleanField(default=True) #This is here in any case we need to deactivate any user
	is_staff = models.BooleanField(default=False) #This checks if the user is staff and has access to the admin site

	objects = UserProfileManager()

	USERNAME_FIELD = 'username' #This is the field that will be used in the login section
	REQUIRED_FIELDS = ['name','email']

	#Helper Functions 
	def get_full_name(self):
		return self.name 

	def get_short_name(self):
		return self.name 

	def __str__(self):
		return self.name