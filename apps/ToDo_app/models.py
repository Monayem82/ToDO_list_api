from django.db import models

class TodoListModel(models.Model):
    task=models.CharField(max_length=40)
    describe=models.TextField(max_length=100)
    is_completed=models.BooleanField(default=False)
    created_to=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    due_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.task}  {self.describe}"
