# Generated by Django 4.0 on 2021-12-29 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_category_options'),
        ('store', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]