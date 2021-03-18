# Generated by Django 3.1.7 on 2021-03-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datos_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODIGO', models.CharField(max_length=150)),
                ('DESCRIPCION', models.CharField(max_length=150)),
                ('ULTIMO_NODO', models.CharField(max_length=150)),
                ('NIVEL', models.CharField(max_length=150)),
                ('CODIGO_PADRE', models.CharField(max_length=150)),
                ('BENEFICIOS_TRIBUTARIOS', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(default=1, max_length=200)),
            ],
        ),
    ]
