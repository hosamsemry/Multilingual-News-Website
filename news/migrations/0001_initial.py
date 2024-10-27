# Generated by Django 5.1.2 on 2024-10-27 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Published At')),
                ('image', models.ImageField(default='news/default.png', upload_to='news/', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Category')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.reporter', verbose_name='Reporter')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Published At')),
                ('image', models.ImageField(default='articles/default.png', upload_to='articles/', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Category')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.reporter', verbose_name='Reporter')),
            ],
        ),
    ]