# Generated by Django 3.2.9 on 2022-07-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20220730_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='image'),
        ),
    ]