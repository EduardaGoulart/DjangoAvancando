# Generated by Django 2.0.1 on 2018-07-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_auto_20180725_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuário pode alterar parâmetro NF-E'), ('ver_dashboard', 'Usuários que podem visualizar o dashboard'), ('permissao3', 'Permissao3'))},
        ),
    ]
