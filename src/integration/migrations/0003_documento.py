# Generated by Django 3.1.7 on 2021-03-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0002_auto_20210320_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=255)),
                ('documento', models.FileField(upload_to='static/documents/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]