from django.contrib import admin
from django.http import HttpRequest
from .models import Project, Skill, Experience, ContactMessage, ExperienceStats, Service, Testimonial,Article
from.models import Certification
# Project Admin
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'technologies', 'link')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'technologies')

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements

# Skill Admin
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements

# Experience Admin
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    search_fields = ('job_title', 'company')
    list_filter = ('company',)

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements

# ContactMessage Admin
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message')

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements

# ExperienceStats Admin
class ExperienceStatsAdmin(admin.ModelAdmin):
    list_display = ('years_of_experience', 'happy_clients', 'completed_projects')
    search_fields = ('years_of_experience', 'happy_clients', 'completed_projects')

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements

# Service Admin
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon_class')
    search_fields = ('title', 'description')

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements

# Testimonial Admin
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession')
    search_fields = ('client_name', 'profession', 'testimonial')

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements
#Article
class ArticleAdmin(admin.ModelAdmin):
    list_display =('title', 'content', 'categories','image')
    search_fields =('title', 'content', 'categories')

    def has_add_permission(self, request):
        return True  # Permet d'ajouter des enregistrements

    def has_change_permission(self, request, obj=None):
        return True  # Permet de modifier des enregistrements

    def has_delete_permission(self, request, obj=None):
        return True  # Permet de supprimer des enregistrements
    
class CertificatAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'date_obtained','badgeImage')
    search_fields = ('title', 'institution', 'date_obtained','badgeImage')

    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request,obj=None):
        return True
    def has_delete_permission(self, request,obj = None):
        return True

# Enregistrement dans l'admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(ExperienceStats, ExperienceStatsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Certification,CertificatAdmin)
