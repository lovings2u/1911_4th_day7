# Generated by Django 2.2.7 on 2019-11-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='creator',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
