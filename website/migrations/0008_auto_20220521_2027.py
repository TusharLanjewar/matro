# Generated by Django 3.0.6 on 2022-05-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_searchs_shortlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchs',
            name='sort',
            field=models.CharField(default='', max_length=20),
        ),
    ]