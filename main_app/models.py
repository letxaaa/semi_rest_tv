from django.db import models
from datetime import date, time, datetime

# Create your models here.
class ShowManager(models.Manager):
    def validate_show(self, postData):
        today = date.today()
        errors = {}

        if len(Show.objects.filter(title = postData['title'])) > 0:
            errors['unique_title'] = "This show already exists!!"

        if len(postData['title']) < 3:
            errors['title'] = "Title must be longer than 2 chars"

        if len(postData['network']) < 4:
            errors['network'] = "Network must be longer than 3 chars"

        if not postData['release_date']:
            errors['release_date'] = "You must enter a date"
        else:
            postDate = datetime.strptime(postData['release_date'], "%Y-%m-%d").date()
            if postDate < today:
                errors['release_date'] = "Release date must be in the future"

        desc_length = len(postData['description'])
        if desc_length:
            if desc_length < 10:
                errors['description'] = "Description must be longer than 10 chars"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    objects = ShowManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)