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

BLOGSTATUS = (
    (0, "Draft"),
    (1, "Publish")
)
BREED = (
    ("German Shepherd", "German Shepherd"),
    ("Bulldog", "Bulldog"),
    ("Labrador Retriever", "Labrador Retriever"),
    ("Golden Retriever", "Golden Retriever"),
    ("French Bulldog", "French Bulldog"),
    ("Siberian Husky", "Siberian Husky"),
    ("Poodle", "Poodle"),
    ("Alaskan Malamute", "Alaskan Malamute"),
    ("Chihuahua", "Chihuahua"),
    ("Border Collie", "Border Collie"),
    ("Afghan Hound", "Afghan Hound"),
    ("Airedale Terrier", "Airedale Terrier"),
    ("Dachshund", "Dachshund"),
    ("Affenpinscher", "Affenpinscher"),
    ("Rottweiler", "Rottweiler"),
    ("American Eskimo Dog", "American Eskimo Dog"),
    ("Bichon Frisé", "Bichon Frisé"),
    ("Great Dane", "Great Dane"),
    ("Maltese dog", "Maltese dog"),
    ("Australian Shepherd", "Australian Shepherd"),
    ("English Cocker Spaniel", "English Cocker Spaniel"),
    ("Chow Chow", "Chow Chow"),
    ("Pomeranian", "Pomeranian"),
    ("Yorkshire Terrier", "Yorkshire Terrier"),
    ("Pembroke Welsh Corgi", "Pembroke Welsh Corgi"),
    ("Cavalier King Charles Spaniel", "Cavalier King Charles Spaniel"),
    ("Anatolian Shepherd Dog", "Anatolian Shepherd Dog"),
    ("Basset Hound", "Basset Hound"),
    ("Newfoundland dog", "Newfoundland dog"),
    ("Belgian Shepherd", "Belgian Shepherd"),
    ("Basenji", "Basenji"),
    ("Havanese", "Havanese"),
    ("Brittany", "Brittany"),
    ("Bullmastiff", "Bullmastiff"),
    ("Boston Terrier", "Boston Terrier"),
    ("Cairn Terrier", "Cairn Terrier"),
    ("Sheltie", "Sheltie"),
    ("Black Russian Terrier", "Black Russian Terrier"),
    ("Bedlington Terrier", "Bedlington Terrier"),
    ("American Pit Bull Terrier", "American Pit Bull Terrier"),
    ("Dobermann", "Dobermann"),
    ("Shiba Inu", "Shiba Inu"),
    ("Shih Tzu", "Shih Tzu"),
    ("Sarabi dog", "Sarabi dog"),
    ("Samoyed", "Samoyed"),
    ("Maltipoo", "Maltipoo"),
    ("Jack Russell Terrier", "Jack Russell Terrier"),
    ("Goldendoodle", "Goldendoodle"),
    ("American Bully", "American Bully"),
    ("Dalmatian", "Dalmatian"),
    ("Akita Inu", "Akita Inu"),
)

# Create your models here.
class Puppy(models.Model):
    title = models.CharField(max_length =150, verbose_name = 'Puppy Name')
    slug = models.SlugField(max_length=200, unique=True, blank = True, null = True)
    puppy_breed = models.CharField(max_length=29, choices=BREED, verbose_name="Breed")
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
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE, null=True, blank=True, related_name='images')
    images = models.ImageField(upload_to="puppy/images")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering  = ['-created_date']

class Offer(models.Model):
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE, related_name='offers')
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
        return self.phone

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, verbose_name="Phone Number")
    address = models.CharField(max_length=200, verbose_name="Home Address")
    def __str__(self):
        return self.phone

# Create a model for the post categories 
class PostCategory(models.Model):
    category_name = models.CharField(max_length = 150, verbose_name = 'Category name')
    category_description = models.TextField(verbose_name = 'Description', blank = True, null = True)
    def __str__(self):
        return self.category_name

# create a model to post on blog 
class BlogPost(models.Model):
    title = models.CharField(max_length =150, verbose_name = 'Post Title')
    slug = models.SlugField(max_length=200, unique=True)
    post_author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name= 'Author')
    post_category = models.ForeignKey(PostCategory, on_delete = models.CASCADE, verbose_name = 'Post Category')
    post_img = models.ImageField(blank = True, null = True, verbose_name = 'Post Featured Image')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_contents = models.TextField(verbose_name = 'Post Contents')
    status = models.IntegerField(choices=BLOGSTATUS, default=0)
    class Meta:
        ordering  = ['-created_date']
    def __str__(self):
        return self.title

class BlogImages(models.Model):
    puppy = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to="blog/images")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering  = ['-created_date']