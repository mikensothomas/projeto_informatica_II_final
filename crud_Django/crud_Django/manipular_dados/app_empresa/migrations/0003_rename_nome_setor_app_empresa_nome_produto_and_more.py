# Generated by Django 4.2.4 on 2023-09-17 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_empresa', '0002_rename_employee_app_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app_empresa',
            old_name='nome_setor',
            new_name='nome_produto',
        ),
        migrations.RenameField(
            model_name='app_empresa',
            old_name='empresa_terceira',
            new_name='quantidade',
        ),
        migrations.RemoveField(
            model_name='app_empresa',
            name='fornecedores',
        ),
        migrations.RemoveField(
            model_name='app_empresa',
            name='funcionarios',
        ),
        migrations.RemoveField(
            model_name='app_empresa',
            name='produtos',
        ),
    ]
