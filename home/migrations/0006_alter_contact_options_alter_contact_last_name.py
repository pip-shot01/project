# Generated by Django 4.0.5 on 2022-06-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_contact_email_alter_contact_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'managed': True, 'verbose_name': 'Contact', 'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
