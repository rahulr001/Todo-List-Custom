# Generated by Django 4.1 on 2022-09-22 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktitle', models.CharField(max_length=50)),
                ('taskdesc', models.TextField()),
                ('unique_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Todolist.user')),
            ],
        ),
    ]