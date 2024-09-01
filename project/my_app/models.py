from django.db import models as m
from rest_framework.generics import ListAPIView

from users.models import User


# Create your models here.



class Note(m.Model):
    title = m.CharField('Title', max_length=50, null=True)
    description = m.CharField('Description', max_length=50, null=True)
    created_at = m.DateTimeField('Created at', auto_now_add=True)
    user_id = m.ForeignKey(User, on_delete=m.CASCADE, null=True)
    status = m.BooleanField("Status", default=False)

    def __str__(self):
        return self.title



