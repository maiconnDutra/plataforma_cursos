# Generated by Django 5.2.1 on 2025-05-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='capa_upload',
            field=models.FileField(blank=True, help_text='Envie uma imagem do seu computador', null=True, upload_to='capas/'),
        ),
    ]
