# Generated by Django 2.2.6 on 2019-10-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_auto_20191007_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='paper_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
