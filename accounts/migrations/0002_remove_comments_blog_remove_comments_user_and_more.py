# Generated by Django 4.0.2 on 2022-03-03 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]