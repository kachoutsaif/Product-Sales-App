from django.urls import path,include
from rest_framework import routers
from .views import *
routes=routers.DefaultRouter()
routes.register('Consommateurs',ConsommateurViewSet,basename='consommateurViews')
routes.register('Produits',ProduitViewSet,basename='produitViewset')
routes.register('Commandes',CommandeViewSet,basename= 'commandeViewset')
routes.register('Fournisseurs',FournisseurViewSet,basename= 'fournisseurViewset')
routes.register('Categories',CategorieViewSet,basename= 'categorieViewset')
routes.register('DetailCommands',DetailCommandeViewSet,basename= 'detailcommandeViewset')
routes.register('Factures',FactureViewSet,basename= 'factureViewset')
routes.register('Offres',OffreViewSet,basename= 'offreViewset')
routes.register('Addresses',AdresseViewSet,basename= 'addresseViewset')
urlpatterns = [
    path('',include(routes.urls)),
]
