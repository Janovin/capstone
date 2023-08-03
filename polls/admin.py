"""In this file, you will see that the models 'Question' and 'Choice' are registered."""
from django.contrib import admin
from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
