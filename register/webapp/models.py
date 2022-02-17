from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Userdata(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=8)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    # profile_photo = models.ImageField(upload_to='profile')
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s %s %s %s " %(self.username, self.last_name,self.date_of_birth,self.address, self.email_id, self.phone)



