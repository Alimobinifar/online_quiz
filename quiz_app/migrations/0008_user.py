# Generated by Django 4.0 on 2021-12-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_remove_answers_four_remove_answers_one_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
    ]