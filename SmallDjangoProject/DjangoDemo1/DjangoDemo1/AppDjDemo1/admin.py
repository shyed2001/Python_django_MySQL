# File name: : DjangoDemo1/AppDjDemo1/admin.py
# Remote URL: 
# Compare this snippet from DjangoDemo1/AppDjDemo1/models.py:


from django.contrib import admin # Import the admin module
from .models import Plan_Tasks, Item, Test, Category, SubCategory, Question, Answer

# Register Plan_Tasks and Item models
admin.site.register(Plan_Tasks)
admin.site.register(Item)

# Custom Admin for Test
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('taste_name_id', 'test_name', 'description')  # Fields to display in the list view
    search_fields = ('test_name', 'taste_name_id')  # Enable search on test name and ID

# Custom Admin for Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categories_name_id', 'test', 'category_name', 'description')
    search_fields = ('category_name', 'categories_name_id')
    list_filter = ('test',)  # Filter by Test in the list view

# Custom Admin for SubCategory
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('snt_id', 'category', 'subcategory_name', 'description')
    search_fields = ('subcategory_name', 'snt_id')
    list_filter = ('category',)  # Filter by Category in the list view

# Custom Admin for Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('q_id', 'subcategory', 'question_text', 'difficulty')
    search_fields = ('q_id', 'question_text')
    list_filter = ('subcategory', 'difficulty')  # Filter by SubCategory and Difficulty

# Custom Admin for Answer
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('ans_id', 'question', 'option_text', 'score_value')
    search_fields = ('option_text',)
    list_filter = ('question',)  # Filter by Question


# Explain the code above in detail, syntax, flow, working principle, data flow,  concepts etc.:
# The code above registers the models Plan_Tasks and Item with the Django admin interface.
# The admin.site.register() method is used to register the models with the admin interface.
# The code also defines custom admin classes for the models Test, Category, SubCategory, Question, and Answer.
# These custom admin classes inherit from the admin.ModelAdmin class.
# The custom admin classes define the list_display, search_fields, and list_filter attributes to customize the admin interface.
# The list_display attribute specifies the fields to display in the list view of the admin interface.
# The search_fields attribute enables search on the specified fields in the admin interface.
# The list_filter attribute adds filters to the list view of the admin interface.
# The @admin.register decorator is used to register the custom admin classes with the admin interface.
# The custom admin classes provide a more user-friendly and organized way to manage the models in the Django admin interface.
# End of file
