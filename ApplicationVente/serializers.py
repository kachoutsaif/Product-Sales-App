from .models import  *
from rest_framework import serializers
class ConsommateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consommateur
        fields='__all__'
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model =Admin
        fields="__all__"
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produit
        fields='__all__'
class  CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Commande
        fields='__all__'
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model =Fournisseur
        fields="__all__"
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categorie
        fields="__all__"
class  DetailCommandeSerializer(serializers.ModelSerializer):
     class Meta:
         model=DetailCommande
         fields="__all__"
class FactureSerializer(serializers.ModelSerializer):
     class Meta:
         model=Facture
         fields="__all__"
class OffreSerializer(serializers.ModelSerializer):
     class Meta:
         model=Offre
         fields="__all__"
class AdresseSerializer(serializers.ModelSerializer):
     class Meta:
         model=Adresse
         fields="__all__"