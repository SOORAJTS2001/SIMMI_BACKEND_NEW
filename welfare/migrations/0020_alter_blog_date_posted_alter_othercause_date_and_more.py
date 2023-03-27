# Generated by Django 4.1.2 on 2023-03-27 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0019_alter_blog_date_posted_alter_othercause_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateField(default=datetime.date(2023, 3, 27)),
        ),
        migrations.AlterField(
            model_name='othercause',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 27)),
        ),
        migrations.AlterField(
            model_name='story',
            name='issue_on',
            field=models.DateField(default=datetime.date(2023, 3, 27)),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 27)),
        ),
    ]
