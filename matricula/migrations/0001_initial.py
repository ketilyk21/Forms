# Generated by Django 5.1.1 on 2024-09-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('genero', models.CharField(max_length=10)),
                ('nacionalidade', models.CharField(max_length=50)),
                ('nome_mae', models.CharField(max_length=100)),
            ],
        ),
    ]
