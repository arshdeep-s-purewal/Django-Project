# Generated by Django 4.1.7 on 2023-03-21 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_date_of_release'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': (('can_publish', 'To publish a blog'),)},
        ),
    ]
