# Generated by Django 3.1.2 on 2020-10-22 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201022_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='images',
            new_name='image',
        ),
    ]
