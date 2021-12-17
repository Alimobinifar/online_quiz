# Generated by Django 4.0 on 2021-12-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='cat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='four',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='questions',
            name='one',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tree',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='questions',
            name='two',
            field=models.CharField(max_length=50),
        ),
    ]