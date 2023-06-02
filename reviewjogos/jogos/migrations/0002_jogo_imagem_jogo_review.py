# Generated by Django 4.2.1 on 2023-06-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='imagem',
            field=models.ImageField(default='Capa do jogo.', upload_to='images'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='review',
            field=models.TextField(default='', help_text='Digite a review do jogo.', max_length=4000),
        ),
    ]
