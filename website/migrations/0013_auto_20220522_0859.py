# Generated by Django 3.0.6 on 2022-05-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_searchs_slist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchs',
            name='slist',
            field=models.CharField(default='a', max_length=20),
        ),
    ]
