# Generated by Django 3.1.7 on 2021-03-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0008_validddd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='status',
            field=models.CharField(blank=True, choices=[('B', 'Blacklist'), ('I', 'Inválido'), ('V', 'Valido'), ('N', 'NÃO PERMITIDO')], max_length=3, null=True),
        ),
    ]
