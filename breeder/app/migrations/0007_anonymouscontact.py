# Generated by Django 3.2.16 on 2023-02-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Contact Message')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
