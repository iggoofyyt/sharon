from django.db import models

class user(models.Model):
    name=models.CharField(max_length=50)
    emaill=models.EmailField()
    pswd=models.CharField(max_length=20)
    cpswd=models.CharField(max_length=20)
    status=models.IntegerField()
    def __str__(self):
        return self.name

class logi(models.Model):
    name = models.CharField(max_length=50)
    pswd = models.CharField(max_length=20)
    status = models.IntegerField()
    def __str__(self):
        return self.name

# class shop(models.Model):
#     n1 = models.IntegerField()
#     n2 = models.IntegerField()
#     n3 = models.IntegerField()
#     n4 = models.IntegerField()
#     name = models.CharField(max_length=50)
#     action = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


class price(models.Model):
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    n3 = models.IntegerField()
    n4 = models.IntegerField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    p1 = models.CharField(max_length=9)
    p2 = models.CharField(max_length=9)
    p3 = models.CharField(max_length=9)
    p4 = models.CharField(max_length=9)
    name = models.CharField(max_length=50)
    amt = models.IntegerField()
    total = models.IntegerField()
    action = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    emaill = models.EmailField()
    proof = models.FileField()
    pswd = models.CharField(max_length=20)
    cpswd = models.CharField(max_length=20)
    status = models.IntegerField()
    action = models.CharField(max_length=30)
    deliver=models.IntegerField()

    def __str__(self):
        return self.name

class detail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    adres = models.CharField(max_length=300)
    phone = models.IntegerField()
    nme = models.CharField(max_length=20)
    action = models.CharField(max_length=30)
    emp = models.CharField(max_length=50)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    amount = models.IntegerField()
    datee = models.DateField()

    def __str__(self):
        return self.nme

class orders(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    action = models.CharField(max_length=30)
    amount = models.IntegerField()
    datee = models.DateField()
    def __str__(self):
        return self.name

class cancel(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    phone = models.IntegerField()
    action = models.CharField(max_length=30)

class concent(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.CharField(max_length=300)
    date = models.DateField()
    def __str__(self):
        return self.name

# -------------------------------- PASSWORD RESET TABLE -------------------------------

class PasswordReset(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


#messages table
class msg(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'

class product(models.Model):
    name=models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.FileField()
    def __str__(self) -> str:
        return f'{self.name}'







# Create your models here.
