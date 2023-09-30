# Generated by Django 4.2.5 on 2023-09-28 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_list', '0001_initial'),
        ('todo_item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_items', to='todo_list.todolist'),
        ),
    ]
