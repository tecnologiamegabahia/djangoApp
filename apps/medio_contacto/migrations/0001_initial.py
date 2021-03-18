# Generated by Django 3.1.7 on 2021-03-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medio_contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODIGO', models.CharField(max_length=150)),
                ('VALOR', models.CharField(max_length=150)),
                ('ESTABLECIMIENTO', models.CharField(max_length=150)),
                ('NUMERO_RUC', models.CharField(max_length=150)),
                ('TIPO_MEDIO_CONTACTO', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(default=1, max_length=200)),
            ],
        ),
    ]