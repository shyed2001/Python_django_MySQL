from django.db import models


# Create your models here.

class Plan_Tasks(models.Model):
    task_name = models.CharField(max_length=150)
    # description = models.CharField(max_length=100)
    # start_date = models.DateField()
    # end_date = models.DateField()
    # status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.task_name
      

class Item(models.Model):
  
    plan_task = models.ForeignKey(Plan_Tasks, on_delete=models.CASCADE)
    plan_task_text = models.CharField(max_length=200)
    # plan_task_completed = models.BooleanField(default=False)
    plan_task_completed = models.BooleanField()
    # item_name = models.CharField(max_length=150)
    # item_description = models.CharField(max_length=100)
    # item_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return str(self.plan_task_text)

