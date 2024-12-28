# Generated by Django 5.1.4 on 2024-12-24 22:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avalicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrelas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Não pode enviar um valor menor que 0.'), django.core.validators.MaxValueValidator(5, 'Não pode enviar o valor maior que 5.')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='avalicoes', to='filmes.filmes')),
            ],
        ),
    ]