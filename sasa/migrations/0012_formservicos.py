# Generated by Django 5.1.1 on 2024-11-14 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sasa', '0011_delete_formservicos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormServicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.IntegerField()),
                ('detalhes', models.TextField()),
                ('data', models.DateField()),
                ('aceita', models.BooleanField(default=None, null=True)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sasa.servicos')),
            ],
        ),
    ]