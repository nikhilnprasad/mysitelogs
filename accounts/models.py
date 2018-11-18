from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import pytz
from datetime import datetime
from django.core.management import call_command
import os
import json


lt = str(datetime.utcnow())

data1 = []

class Activity_Log(models.Model):
	username = models.CharField(max_length = 150, blank = True)
	date_time = models.DateTimeField(auto_now_add = True, blank = True)
	activity = models.CharField(max_length = 50, blank = True)

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.date_time, self.username, self.activity)


	@receiver(user_logged_in)
	def user_logged_in_callback(sender, request, user, **kwargs):
		Activity_Log.objects.create(username=user.username, date_time = lt, activity='user_logged_in')


	@receiver(user_logged_out)
	def user_logged_out_callback(sender, request, user, **kwargs):  
		Activity_Log.objects.create(username=user.username, date_time = lt, activity='user_logged_out')


	@receiver(user_login_failed)
	def user_login_failed_callback(sender, credentials, **kwargs):
		Activity_Log.objects.create(username=credentials.get('username', None), date_time = lt, activity='user_login_failed')
		
