# Generated by Django 5.1.1 on 2024-10-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0009_solicitacao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='solicitacao',
        ),
        migrations.AddField(
            model_name='formservicos',
            name='aceita',
            field=models.BooleanField(default=None, null=True),
        ),
    ]