from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Define groups
groups = {
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    "Editors": ["can_create", "can_edit"],
    "Viewers": ["can_view"]
}

book_content_type = ContentType.objects.get_for_model(Book)

for group_name, perms in groups.items():
    group, created = Group.objects.get_or_create(name=group_name)
    for perm_codename in perms:
        perm = Permission.objects.get(codename=perm_codename, content_type=book_content_type)
        group.permissions.add(perm)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    ordering = ('title',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )




admin.site.register(CustomUser, CustomUserAdmin)
