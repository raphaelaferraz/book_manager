# Generated by Django 4.0.1 on 2022-01-13 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_gerenciador_de_livros', '0010_statuslivro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='situacao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_gerenciador_de_livros.statuslivro'),
            preserve_default=False,
        ),
    ]
