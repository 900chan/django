from django.contrib import admin
from rest_framework.views import APIView
from .models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass