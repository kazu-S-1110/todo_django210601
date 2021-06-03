from django.db import models

CHOICE = ("danger", "high"), ("warning", "normal"), ("primary", "low")


class TodoModel(models.Model):  # model.Modelを継承して作成している
    title = models.CharField(max_length=30)
    memo = models.TextField()
    priority = models.CharField(max_length=30,
                                choices=CHOICE
                                )
    duedate = models.DateField()

    def __str__(self):
        return self.title
