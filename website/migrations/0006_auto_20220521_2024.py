# Generated by Django 3.0.6 on 2022-05-22 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20220521_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortlist',
            name='shortlist',
        ),
        migrations.DeleteModel(
            name='searchs',
        ),
        migrations.DeleteModel(
            name='shortlist',
        ),
    ]