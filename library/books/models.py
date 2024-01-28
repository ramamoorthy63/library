from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    mark = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    is_correct=models.BooleanField
    option1 = models.CharField(max_length=60, default=None)
    option2 = models.CharField(max_length=60, default=None)
    option3 = models.CharField(max_length=60, default=None)
    option4 = models.CharField(max_length=60, default=None)
    correct_answer = models.CharField(max_length=60,)
    added_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question} : (a). {self.option1} (b). {self.option2} (c). {self.option3} (d). {self.option4} "