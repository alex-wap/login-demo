from __future__ import unicode_literals

from django.db import models

# we need re for regex
# we need bcrypt for passwords
import re, bcrypt

# UserManager is a custom Manager
class UserManager(models.Manager):

  def login(self, postData):
    print "inside login"
    messages = []
    # error if email length < 1
    # error if password length < 1
    # if no error messages
      # query db to get user.password
      # check user.password against hashed password
      # if it works, return None
      # else, return error message for incorrect password
    # return errors (messages)
    pass

  def register(self, postData):
    print "inside register"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    messages = []
    # error if first is blank
    # error if first is not 2 chars
    # error if last is blank
    # error if last is not 2 chars
    # error if first or last is not alpha
    # error if email is blank
    # error if email is invalid
    # error if password is blank
    # error if password is not 8 chars
    # error if password doesnt match confirm
    # check if email exists already
    # if email exists, error
    # if no errors
      # hash password
      # print "create user"
      # return None
    # return errors (messages)
    pass

class User(models.Model):
  first = models.CharField(max_length=45)
  last = models.CharField(max_length=45)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  # The default Manager for the model is objects, 
  # and it is auto created if you don't specify a custom manager.
  # We can overwrite it below: 
  objects = UserManager()