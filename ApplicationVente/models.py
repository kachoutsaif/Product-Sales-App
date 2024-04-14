from django.db import models
from django.contrib.auth.models import User

#class visiteur
class Visiteur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.IntegerField(null=True, blank=True)  
    date_visite = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Visiteur'
    def __str__(self):
        return f"{self.nom} - {self.prenom}"

    
#class adresse 
class Adresse(models.Model):
    adresse_ligne1 = models.CharField(max_length=255)
    adresse_ligne2 = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    class Meta:
        db_table = 'Adresse-Consommateur'
    def __str__(self):
        return f"{self.adresse_ligne1}, {self.ville}, {self.code_postal}"    


#class consommateur 
class Consommateur(Visiteur):
    mot_passe = models.CharField(max_length=16)
    adresse_consommateur = models.OneToOneField(Adresse, on_delete=models.CASCADE, related_name='consommateur', null=True)
    STATUT_CHOICES = [
        ('allergiques ', 'Allergiques '),
        ('asthmatique', 'Asmatique'),
        ('normal', 'Normal'),
    ]
    type_consommateur = models.CharField(max_length=16,choices=STATUT_CHOICES, default='normal')
    class Meta:
        db_table = 'Consommateur'
    def __str__(self):
        return f"{self.nom} - {self.prenom}"

    


#class administratuer 
class Admin(Visiteur):
    mot_passe = models.CharField(max_length=16)
    class Meta:
        db_table = 'Administrateur'
    def __str__(self):
        return f"{self.nom} - {self.prenom}"

    
    

#class fournisseur  
class Fournisseur(models.Model):
    id_fourn = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adresse_fourn = models.CharField(max_length=255)
    telephone = models.IntegerField(null=False)
    email  = models.EmailField(unique=True)
    class Meta:
        db_table = 'Fournissuer'
    def __str__(self):
        return self.nom



#class categories
class Categorie(models.Model):
    id_catg = models.AutoField(primary_key=True)
    libelle_catg = models.CharField(max_length=30, default='')
    class Meta:
        db_table = 'Categorie'
    def __str__(self):
        return self.libelle_catg


#class produit 
class Produit(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField()
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE, related_name='produits')
    consult_prod = models.ManyToManyField(Visiteur)
    comm_prod = models.ManyToManyField(Consommateur,through='Commande',through_fields=('produit','consommateur'), related_name='commandes_produit')
    class Meta:
        db_table = 'Produit'
    def __str__(self):
        return self.nom_prod

    
#class commande 
class Commande(models.Model):
    id_com = models.AutoField(primary_key=True)
    consommateur = models.ForeignKey(Consommateur, on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    date_comm = models.DateTimeField(auto_now_add=True)
    STATUT_CHOICES = [
        ('en_attente', 'En Attente'),
        ('validee', 'Validée'),
        ('annulee', 'Annulée'),
    ]
    statut_commd = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    class Meta:
        db_table = 'Commande'
    def __str__(self):
        return f"Commande {self.consommateur.nom} ({self.produit.nom_prod})"



#class detail-commande
class DetailCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'DetailCommande'
    def __str__(self):
        return f"{self.commande}"
    def montant_total(self):
        return self.quantite * self.prix_unitaire


#class facture 
class Facture(models.Model):
    id_fact = models.AutoField(primary_key=True)
    date_facture = models.DateField()
    remise = models.DecimalField(max_digits=5, decimal_places=2)
    Detail_Commande = models.OneToOneField(DetailCommande,on_delete=models.CASCADE, related_name='Paiement', null=True)
    class Meta:
        db_table = 'Facture'
    def __str__(self):
        return self.date_facture



#class offre
class Offre(models.Model):
    id_offr = models.AutoField(primary_key=True)
    date_debut_offre = models.DateField()
    date_fin_offre = models.DateField()
    name = models.CharField(max_length=255)
    offre_prod = models.ManyToManyField(Produit)
    class Meta:
        db_table = 'Offre'
    def __str__(self):
        return self.name
