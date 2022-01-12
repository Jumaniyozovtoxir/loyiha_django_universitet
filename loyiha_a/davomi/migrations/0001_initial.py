# Generated by Django 4.0.1 on 2022-01-12 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guruhlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kursantlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=400)),
                ('familiya', models.CharField(max_length=400)),
                ('guruh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='davomi.guruhlar')),
            ],
        ),
    ]
