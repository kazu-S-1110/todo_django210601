from django.db import models


class TodoModel(models.Model):  # model.Modelを継承して作成している
    title = models.CharField(max_length=30)
    memo = models.TextField()

    def __str__(self):
        return self.title