from django.contrib import admin
from .models import Inscription

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom_prenom', 'telephone', 'date_inscription')
    search_fields = ('nom_prenom', 'telephone')
    list_filter = ('date_inscription',)
