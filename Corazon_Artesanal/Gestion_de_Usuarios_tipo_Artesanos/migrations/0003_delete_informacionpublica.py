# Generated by Django 4.2.5 on 2023-12-01 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_de_Inventario', '0002_alter_obra_id_artesano'),
        ('Gestion_de_Usuarios_tipo_Artesanos', '0002_artesano_delete_informacionprivada'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InformacionPublica',
        ),
    ]
