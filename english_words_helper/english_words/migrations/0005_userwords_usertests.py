# Generated by Django 4.1.7 on 2023-03-09 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('english_words', '0004_irregularverbs'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_word', models.CharField(max_length=64)),
                ('ukraine_word', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_in_test', models.IntegerField(default=0)),
                ('all_in_choice', models.IntegerField(default=0)),
                ('true_in_test', models.IntegerField(default=0)),
                ('true_in_choice', models.IntegerField(default=0)),
                ('false_in_test', models.IntegerField(default=0)),
                ('false_in_choice', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
