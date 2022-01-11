from django.db import models


class TodoItem(models.Model):
    content = models.TextField()

    def __str__(self):
        return str(self.content)
