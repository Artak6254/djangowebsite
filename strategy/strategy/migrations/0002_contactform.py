# Generated by Django 5.1.6 on 2025-02-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=70)),
                ('user_message', models.TextField()),
            ],
        ),
    ]
