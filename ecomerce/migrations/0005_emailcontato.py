# Generated by Django 3.2.6 on 2021-12-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0004_produto_ativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]
