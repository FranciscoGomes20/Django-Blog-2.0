from django.contrib import admin
from .models import Post, Contact

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'create_date')
    list_filter = ('author', )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'create_date')