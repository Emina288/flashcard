from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    learned = models.BooleanField(default=False)
    author = models.CharField(max_length=120)
    category = models.CharField(max_length=120, default="")

    def _str_(self):
        return self.question
