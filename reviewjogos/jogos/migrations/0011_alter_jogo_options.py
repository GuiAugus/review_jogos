# Generated by Django 4.2.1 on 2023-06-04 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0010_alter_jogo_plataforma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogo',
            options={'ordering': ['-data_publicacao']},
        ),
    ]
