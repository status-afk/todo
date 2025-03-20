from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    todo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)





    def __str__(self):
        return f"{self.user} {self.todo} {self.is_completed}"