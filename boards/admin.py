from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
	pass