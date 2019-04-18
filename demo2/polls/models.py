from django.db import models


class Question(models.Model):
    qname = models.CharField(max_length=255)

    def __str__(self):
        return self.qname


class Choose(models.Model):
    cname = models.CharField(max_length=20)
    cvote = models.IntegerField(default=0)
    cques = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

