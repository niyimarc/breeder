# Generated by Django 3.2.16 on 2023-02-04 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_puppy_dob'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='images',
            name='puppy',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='Puppy',
        ),
        migrations.RemoveField(
            model_name='puppy',
            name='puppy_breed',
        ),
        migrations.DeleteModel(
            name='Breed',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='Puppy',
        ),
    ]
