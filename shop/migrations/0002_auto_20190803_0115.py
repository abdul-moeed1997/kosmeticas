# Generated by Django 2.2.4 on 2019-08-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender_catagory',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=6),
        ),
    ]
