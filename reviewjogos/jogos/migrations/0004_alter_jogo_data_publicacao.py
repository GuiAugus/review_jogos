# Generated by Django 4.2.1 on 2023-06-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0003_jogo_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
