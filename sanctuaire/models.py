from django.db import models

class Inscription(models.Model):
    nom_prenom = models.CharField(max_length=100, verbose_name="Nom & Prénom")
    telephone = models.CharField(max_length=20, unique=True, verbose_name="Téléphone")
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_prenom} - {self.telephone}"
