# Generated by Django 4.1.2 on 2022-12-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_commonabouttable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Advisory_board',
        ),
        migrations.DeleteModel(
            name='Founders',
        ),
        migrations.DeleteModel(
            name='Senior_management_committee',
        ),
        migrations.DeleteModel(
            name='Senior_technical_committee',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.RemoveField(
            model_name='commonabouttable',
            name='insta_id',
        ),
        migrations.RemoveField(
            model_name='commonabouttable',
            name='meta_id',
        ),
        migrations.RemoveField(
            model_name='commonabouttable',
            name='tweet_id',
        ),
        migrations.AddField(
            model_name='commonabouttable',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='commonabouttable',
            name='fbid',
            field=models.URLField(default='https://www.facebook.com/Meta/'),
        ),
        migrations.AddField(
            model_name='commonabouttable',
            name='instaid',
            field=models.URLField(default='https://www.instagram.com/'),
        ),
        migrations.AddField(
            model_name='commonabouttable',
            name='tweetid',
            field=models.URLField(default='https://twitter.com/'),
        ),
        migrations.AlterField(
            model_name='commonabouttable',
            name='img',
            field=models.ImageField(upload_to='about/'),
        ),
        migrations.AlterField(
            model_name='commonabouttable',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='commonabouttable',
            name='position',
            field=models.CharField(max_length=80),
        ),
    ]
