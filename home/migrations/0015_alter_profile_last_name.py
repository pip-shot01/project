# Generated by Django 4.0.5 on 2022-06-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_profile_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
