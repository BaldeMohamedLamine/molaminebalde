from django.contrib import admin
from .models import User, Profile, SocialProfile

class ProjectUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'aprpos', 'birthday', 'degree', 'address', 'freelance', 'phone', 'freelance')
    list_filter = ('email', 'username', )
    search_fields = ('email', 'first_name', 'last_name')  # 'title', 'description', 'technologies' ne sont pas dans le modèle User

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'biography', 'contact_info')
    list_filter = ('user', )
    search_fields = ('user__username', 'biography')

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True

class AdminSocialProfile(admin.ModelAdmin):
    list_display = ('user', 'platform', 'url')
    list_filter = ('user', 'platform')
    search_fields = ('user__username', 'platform')

    def has_add_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return True

# Enregistrement des modèles dans l'admin
admin.site.register(User, ProjectUserAdmin)
admin.site.register(Profile, AdminProfile)
admin.site.register(SocialProfile, AdminSocialProfile)
