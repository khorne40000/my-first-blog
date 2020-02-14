
# Einbinden von Code aus anderen Dateinen
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #models.Model gibt an, das es sich um ein Django-Model handelt und in der DB gespeichert werden soll
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title