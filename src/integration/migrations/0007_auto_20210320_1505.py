# Generated by Django 3.1.7 on 2021-03-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0006_auto_20210320_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='operadora',
            field=models.CharField(blank=True, choices=[('CLARO', 'CLARO'), ('NEXTEL', 'NEXTEL'), ('OI', 'OI'), ('TIM', 'TIM'), ('VIVO', 'VIVO')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='status',
            field=models.CharField(blank=True, choices=[('B', 'Blacklist'), ('I', 'Inválido'), ('V', 'Valido')], max_length=3, null=True),
        ),
    ]
