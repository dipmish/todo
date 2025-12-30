from django.db import models

class Todo(models.Model):
    # t_id explicitly (instead of default id)
    t_id = models.AutoField(primary_key=True)
    todo_name = models.CharField(max_length=255)

    class Meta:
        db_table = "todo"   # table name fixed as "todo"

    def __str__(self):
        return self.todo_name
