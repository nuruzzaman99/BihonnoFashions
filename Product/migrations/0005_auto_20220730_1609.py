# Generated by Django 3.2.9 on 2022-07-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20220730_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='image/categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='image/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='image/products'),
        ),
    ]