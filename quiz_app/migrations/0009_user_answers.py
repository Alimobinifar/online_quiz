# Generated by Django 4.0 on 2021-12-17 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0008_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=15)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.answers')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='quiz_app.user')),
            ],
        ),
    ]
