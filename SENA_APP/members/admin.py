from django.contrib import admin  # pyright: ignore[reportMissingImports]
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date", "Documento", "phone", "joined_date")
  
admin.site.register(Member, MemberAdmin)