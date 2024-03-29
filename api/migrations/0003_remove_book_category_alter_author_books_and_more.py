# Generated by Django 4.2.1 on 2023-05-25 13:09

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_book_author_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, related_name='author', to='api.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book')),
            ],
        ),
    ]
