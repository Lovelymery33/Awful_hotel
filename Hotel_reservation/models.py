from django.db import models
class Product(models.Model):
    APARTMENT_CHOICES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),  
        ('suite', 'Suite'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    apartment_type = models.CharField(max_length=10, choices=APARTMENT_CHOICES)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    type_apartment = models.CharField(max_length=50, default='single', choices=APARTMENT_CHOICES)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'
        ordering = ['is_available', 'name']
        
class Reservation(models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ]
    apartament = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Reservation for {self.name} - {self.product.name}"
