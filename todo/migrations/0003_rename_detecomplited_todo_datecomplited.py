# Generated by Django 4.0.3 on 2022-03-10 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_detecomplited'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='detecomplited',
            new_name='datecomplited',
        ),
    ]
