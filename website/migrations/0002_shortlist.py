# Generated by Django 3.0.6 on 2022-05-21 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shortlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.searchs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shortlist',
            },
        ),
    ]
