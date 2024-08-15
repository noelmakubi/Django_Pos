from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# People Model
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    # Can be used for customers, suppliers, or employees

    def __str__(self):
        return self.name

# Sale Model
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    sold_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    customer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchases')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Sale of {self.product.name} on {self.sale_date}'

# Purchase Model
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchased_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchases_made')
    supplier = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='supplied_products')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Purchase of {self.product.name} on {self.purchase_date}'

# Return Model
class Return(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    handled_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='returns_handled')

    def __str__(self):
        return f'Return of {self.sale.product.name} on {self.return_date}'

# Report Model
class Report(models.Model):
    report_type = models.CharField(max_length=100)
    generated_on = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    generated_by = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='reports_generated')

    def __str__(self):
        return f'Report {self.report_type} generated on {self.generated_on}'
