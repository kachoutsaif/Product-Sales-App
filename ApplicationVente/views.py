from django.shortcuts import render
from rest_framework import viewsets
from  .models import *  
from .serializers import ConsommateurSerializer
from .serializers import ProduitSerializer
from .serializers import CommandeSerializer
from .serializers import FournisseurSerializer
from .serializers import CategorieSerializer
from .serializers import DetailCommandeSerializer
from .serializers import FactureSerializer
from .serializers import OffreSerializer
from .serializers import AdresseSerializer

class ConsommateurViewSet(viewsets.ModelViewSet):
    queryset=Consommateur.objects.all()
    serializer_class=ConsommateurSerializer
    #http_method_names=['get','post']
class ProduitViewSet(viewsets.ModelViewSet):
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer
class CommandeViewSet(viewsets.ModelViewSet):
    queryset=Commande.objects.all()
    serializer_class=CommandeSerializer
class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
class CategorieViewSet(viewsets.ModelViewSet):
    queryset=Categorie.objects.all()
    serializer_class=CategorieSerializer
class DetailCommandeViewSet(viewsets.ModelViewSet):
    queryset=DetailCommande.objects.all()
    serializer_class=DetailCommandeSerializer
class FactureViewSet(viewsets.ModelViewSet):
    queryset=Facture.objects.all()
    serializer_class=FactureSerializer
class OffreViewSet(viewsets.ModelViewSet):
    queryset=Offre.objects.all()
    serializer_class=OffreSerializer
class AdresseViewSet(viewsets.ModelViewSet):
    queryset=Adresse.objects.all()
    serializer_class=AdresseSerializer


