from django.shortcuts import render, redirect
from .models import Inscription
import urllib.parse

def index(request):
    if request.method == 'POST':
        nom_prenom = request.POST.get('nom_prenom', '').strip()
        indicatif = request.POST.get('indicatif', '').strip()
        telephone = request.POST.get('telephone', '').strip()
        telephone_complet = f"{indicatif} {telephone}"

        if Inscription.objects.filter(telephone=telephone_complet).exists():
            return render(request, 'sanctuaire/index.html', {
                'erreur': 'Ce numéro de téléphone est déjà inscrit.'
            })

        Inscription.objects.create(
            nom_prenom=nom_prenom,
            telephone=telephone_complet
        )
        return redirect('merci')
    return render(request, 'sanctuaire/index.html')

def merci(request):
    import urllib.parse
    message = "Bonjour, je souhaite m'inscrire au Sanctuaire de Vie. Dans l'attente de votre retour, merci."
    message_encode = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/2250709199433?text={message_encode}"
    return render(request, 'sanctuaire/merci.html', {'whatsapp_url': whatsapp_url})
