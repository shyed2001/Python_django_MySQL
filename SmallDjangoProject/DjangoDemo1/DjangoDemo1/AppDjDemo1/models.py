# File name: : DjangoDemo1/AppDjDemo1/models.py
# Remote URL: 
# Compare this snippet from DjangoDemo1/AppDjDemo1/admin.py:

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



# Choices for test_name field in the Test model
class TestNameChoices(models.TextChoices):
    EQ_EI = 'EQ_EI', 'EQ_EI'
    IQ_IT = 'IQ_IT', 'IQ_IT'
    SI = 'SI', 'SI'
    GKT = 'GKt', 'GKt'
    PT = 'PT', 'PT'
    JT_RT = 'JT_RT', 'JT_RT'
    AA_MT = 'AA_MT', 'AA_MT'
    CT = 'CT', 'CT'

# Choices for difficulty levels in the Question model
class DifficultyChoices(models.TextChoices):
    NA_Null = 'none', 'None'
    EASY = 'easy', 'Easy'
    MEDIUM = 'medium', 'Medium'
    HARD = 'hard', 'Hard'


class Test(models.Model):
    taste_name_id = models.CharField(max_length=25, primary_key=True, unique=True)  # Unique identifier
    test_name = models.CharField(max_length=10, choices=TestNameChoices.choices, default=TestNameChoices.EQ_EI)
    description = models.TextField()

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.test_name


class Category(models.Model):
    categories_name_id = models.CharField(max_length=25, primary_key=True, unique=True)  # Unique identifier
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='categories')  # Foreign key to Test
    category_name = models.CharField(max_length=125)
    description = models.TextField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    snt_id = models.CharField(max_length=25, primary_key=True, unique=True)  # Unique identifier
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')  # Foreign key to Category
    subcategory_name = models.CharField(max_length=125)
    description = models.TextField()

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.subcategory_name


class Question(models.Model):
    q_id = models.CharField(max_length=25, primary_key=True, unique=True)  # Unique identifier
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='questions')  # Foreign key to SubCategory
    question_text = models.TextField()
    difficulty = models.CharField(max_length=6, choices=DifficultyChoices.choices, default=DifficultyChoices.MEDIUM)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f"Question {self.q_id} - {self.difficulty}"


class Answer(models.Model):
    ans_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # Foreign key to Question
    option_text = models.TextField()
    score_value = models.IntegerField()

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return f"Answer {self.ans_id} for Question {self.question.q_id}"

# Explain the code above in detail, syntax, flow, working principle, data flow,  concepts etc.: 
# The code above defines the models Plan_Tasks, Item, Test, Category, SubCategory, Question, and Answer.
# The Plan_Tasks model represents a task with a task_name field.
# The Item model represents an item with a plan_task, plan_task_text, and plan_task_completed fields.
# The Test model represents a test with a taste_name_id, test_name, and description fields. 
# The Category model represents a category with a categories_name_id, test, category_name, and description fields.
# 