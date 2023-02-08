from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
        ("Available", "Available"),
        ("Pending", "Pending"),
        ("Sold out", "Sold out")
    )
ANSWER = (
    ("Yes", "Yes"),
    ("No", "No")
)

PUPPYHOUSE = (
    ("Inside", "Inside"),
    ("Outside", "Outside")
)
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Any Gender", "Any Gender")
)
class Breed(models.Model):
    breed_name = models.CharField(max_length = 150, verbose_name = 'Breed name')
    description = models.TextField(verbose_name = 'Description', blank = True, null = True)
    def __str__(self):
        return self.breed_name

# Create your models here.
class Puppy(models.Model):
    title = models.CharField(max_length =150, verbose_name = 'Puppy Name')
    slug = models.SlugField(max_length=200, unique=True, blank = True, null = True)
    puppy_breed = models.ForeignKey(Breed, on_delete = models.CASCADE, verbose_name = 'Post Category')
    banner = models.ImageField(upload_to="puppy/banner", verbose_name = 'Puppy Featured Image')
    dob = models.DateField()
    description = models.TextField(verbose_name = 'Post Contents')
    price = models.IntegerField()
    sire = models.CharField(max_length =150, blank = True, null = True)
    dam = models.CharField(max_length =150, blank = True, null = True)
    male = models.IntegerField()
    female = models.IntegerField()
    health_vaccine = models.CharField(max_length =150)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default="Available")
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.title

class Images(models.Model):
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to="puppy/images")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering  = ['-created_date']


class Offer(models.Model):
    Puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE, related_name='offers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Offer {} by {}'.format(self.message, self.user)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length = 150, verbose_name = "Subject")
    message = models.TextField(verbose_name = "Contact Message")
    def __str__(self):
        return self.subject

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE)
    address = models.TextField(verbose_name = "Contact Message")
    phone = models.TextField(verbose_name="Phone Number")
    ever_own_pet = models.CharField(max_length=3, choices=ANSWER, default="Yes", verbose_name="Ever own a pet?")
    ever_own_dog = models.CharField(max_length=3, choices=ANSWER, default="Yes", verbose_name="Ever own a dog?")
    home_type = models.TextField(verbose_name="Type of home")
    home_fenced = models.CharField(max_length=3, choices=ANSWER, verbose_name="Is your house fenced?")
    puppy_home = models.CharField(max_length=7, choices=PUPPYHOUSE, verbose_name="Will the puppy be housed inside or outside?")
    care_taker = models.CharField(max_length=100, verbose_name="Who will be the primary caretaker of the dog?")
    puppy_gender = models.CharField(max_length=10, choices=GENDER, verbose_name="Are you interested in a male or female puppy?")
    about_yourself = models.TextField(verbose_name="Is there anything else that you would like to tell us about yourself and your family?")
    question = models.TextField(verbose_name="Do you have any question for us?")
    def __str__(self):
        return self.user