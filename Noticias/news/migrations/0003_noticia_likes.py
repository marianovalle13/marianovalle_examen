# Generated by Django 2.0.6 on 2018-07-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_comentario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='likes',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
