from django.db import models

# Create your models here.

#promotion - product  une relation de many to many
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount= models.FloatField()


class Collection (models.Model):
    titre = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='featured_in_collections')
    def __str__(self):
        return self.titre


class Product(models.Model):
    title= models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    #9999.99
    unit_price= models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)


class Custumer(models.Model):
    MEMBERSHIP_BRONZE ='B'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_GOLD ='G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone= models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 , choices=MEMBERSHIP_CHOICES , default=MEMBERSHIP_BRONZE)
    #pour afficher les customer dans la page admin avec c est noms
    def __str__(self):
        return self.first_name
    #default ordering
    class Meta :
        ordering =['first_name']


class Order(models.Model):
    PAYEMENT_STATUS_PENDING = 'P'
    PAYEMENT_STATUS_PENDING = 'C'
    PAYEMENT_STATUS_PENDING = 'F'

    PAYEMENT_STATUS_CHOICES = [
        (PAYEMENT_STATUS_PENDING,'Pending'),
        (PAYEMENT_STATUS_PENDING , 'Complete'),
        (PAYEMENT_STATUS_PENDING , 'Failed')
    ]

    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1 , choices=PAYEMENT_STATUS_CHOICES , default=PAYEMENT_STATUS_PENDING
    )
    custumer = models.ForeignKey(Custumer,on_delete=models.PROTECT)


class Adress(models.Model):
    street= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    #for relation one to one : 
    
    #custumer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

    #FOR RELATION ONE TO MANY :
    custumer = models.ForeignKey(Custumer, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.PROTECT)
    product= models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =models.PositiveSmallIntegerField()

class Reviews (models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)