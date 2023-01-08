# Generated by Django 4.1.4 on 2023-01-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsportal_apps', '0002_category_post_author_user_postcategory_post_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
        migrations.AddField(
            model_name='author',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]