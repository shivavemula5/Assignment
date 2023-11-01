from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    def __str__(self):
        return f'{self.text[:]}'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    def __str__(self):
        return f'{self.text[:]}'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    def __str__(self):
        return f'liked by {self.user} for answer : {self.answer.text[:100]}'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'answer')
