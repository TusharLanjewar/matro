# Generated by Django 3.0.6 on 2022-05-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0003_alter_paytmhistory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]