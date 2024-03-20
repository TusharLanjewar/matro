# Generated by Django 3.0.6 on 2022-05-22 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_shortlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchs',
            name='sort',
            field=models.CharField(default='no', max_length=20),
        ),
        migrations.AlterField(
            model_name='shortlist',
            name='shortlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dd', to='website.searchs'),
        ),
    ]
