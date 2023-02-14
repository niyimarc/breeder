# Generated by Django 3.2.16 on 2023-02-13 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('service_type', models.CharField(max_length=50, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Contact Message')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='Category name')),
                ('category_description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Puppy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Puppy Name')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('puppy_breed', models.CharField(choices=[('German Shepherd', 'German Shepherd'), ('Bulldog', 'Bulldog'), ('Labrador Retriever', 'Labrador Retriever'), ('Golden Retriever', 'Golden Retriever'), ('French Bulldog', 'French Bulldog'), ('Siberian Husky', 'Siberian Husky'), ('Poodle', 'Poodle'), ('Alaskan Malamute', 'Alaskan Malamute'), ('Chihuahua', 'Chihuahua'), ('Border Collie', 'Border Collie'), ('Afghan Hound', 'Afghan Hound'), ('Airedale Terrier', 'Airedale Terrier'), ('Dachshund', 'Dachshund'), ('Affenpinscher', 'Affenpinscher'), ('Rottweiler', 'Rottweiler'), ('American Eskimo Dog', 'American Eskimo Dog'), ('Bichon Frisé', 'Bichon Frisé'), ('Great Dane', 'Great Dane'), ('Maltese dog', 'Maltese dog'), ('Australian Shepherd', 'Australian Shepherd'), ('English Cocker Spaniel', 'English Cocker Spaniel'), ('Chow Chow', 'Chow Chow'), ('Pomeranian', 'Pomeranian'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Pembroke Welsh Corgi', 'Pembroke Welsh Corgi'), ('Cavalier King Charles Spaniel', 'Cavalier King Charles Spaniel'), ('Anatolian Shepherd Dog', 'Anatolian Shepherd Dog'), ('Basset Hound', 'Basset Hound'), ('Newfoundland dog', 'Newfoundland dog'), ('Belgian Shepherd', 'Belgian Shepherd'), ('Basenji', 'Basenji'), ('Havanese', 'Havanese'), ('Brittany', 'Brittany'), ('Bullmastiff', 'Bullmastiff'), ('Boston Terrier', 'Boston Terrier'), ('Cairn Terrier', 'Cairn Terrier'), ('Sheltie', 'Sheltie'), ('Black Russian Terrier', 'Black Russian Terrier'), ('Bedlington Terrier', 'Bedlington Terrier'), ('American Pit Bull Terrier', 'American Pit Bull Terrier'), ('Dobermann', 'Dobermann'), ('Shiba Inu', 'Shiba Inu'), ('Shih Tzu', 'Shih Tzu'), ('Sarabi dog', 'Sarabi dog'), ('Samoyed', 'Samoyed'), ('Maltipoo', 'Maltipoo'), ('Jack Russell Terrier', 'Jack Russell Terrier'), ('Goldendoodle', 'Goldendoodle'), ('American Bully', 'American Bully'), ('Dalmatian', 'Dalmatian'), ('Akita Inu', 'Akita Inu')], max_length=29, verbose_name='Breed')),
                ('banner', models.ImageField(upload_to='puppy/banner', verbose_name='Puppy Featured Image')),
                ('dob', models.DateField()),
                ('description', models.TextField(verbose_name='Post Contents')),
                ('price', models.IntegerField()),
                ('sire', models.CharField(blank=True, max_length=150, null=True)),
                ('dam', models.CharField(blank=True, max_length=150, null=True)),
                ('male', models.IntegerField()),
                ('female', models.IntegerField()),
                ('health_vaccine', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Pending', 'Pending'), ('Sold out', 'Sold out')], default='Available', max_length=10)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, verbose_name='Phone Number')),
                ('address', models.CharField(max_length=200, verbose_name='Home Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('puppy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='app.puppy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='puppy/images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('puppy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.puppy')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Contact Message')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Post Title')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('post_img', models.ImageField(upload_to='', verbose_name='Post Featured Image')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('post_contents', models.TextField(verbose_name='Post Contents')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.postcategory', verbose_name='Post Category')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='blog/images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('puppy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.blogpost')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Contact Message')),
                ('phone', models.TextField(verbose_name='Phone Number')),
                ('ever_own_pet', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3, verbose_name='Ever own a pet?')),
                ('ever_own_dog', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3, verbose_name='Ever own a dog?')),
                ('home_type', models.TextField(verbose_name='Type of home')),
                ('home_fenced', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is your house fenced?')),
                ('puppy_home', models.CharField(choices=[('Inside', 'Inside'), ('Outside', 'Outside')], max_length=7, verbose_name='Will the puppy be housed inside or outside?')),
                ('care_taker', models.CharField(max_length=100, verbose_name='Who will be the primary caretaker of the dog?')),
                ('puppy_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Any Gender', 'Any Gender')], max_length=10, verbose_name='Are you interested in a male or female puppy?')),
                ('about_yourself', models.TextField(verbose_name='Is there anything else that you would like to tell us about yourself and your family?')),
                ('question', models.TextField(verbose_name='Do you have any question for us?')),
                ('puppy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.puppy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
