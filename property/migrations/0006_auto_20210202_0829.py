# Generated by Django 3.1.6 on 2021-02-02 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
    ]
