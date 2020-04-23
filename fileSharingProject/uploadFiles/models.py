from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField

# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class uploadFile(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)

	filename = models.CharField(max_length = 200)
	file = models.FileField(upload_to=user_directory_path)


	isprivate = models.BooleanField(default=False)
	give_access_to = ArrayField(models.CharField(max_length=200), blank=True)


	tags = ArrayField(models.CharField(max_length=200))
	year = models.IntegerField(blank = True)
	semister = models.IntegerField(blank = True)
	subject = models.CharField(max_length = 200, blank = True)
	lecturer_name = models.CharField(max_length = 200, blank = True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)