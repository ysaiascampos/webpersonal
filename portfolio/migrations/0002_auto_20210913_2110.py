# Generated by Django 3.2.7 on 2021-09-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyect',
            options={'ordering': ['-created'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AddField(
            model_name='proyect',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='image',
            field=models.ImageField(upload_to='proyects', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición'),
        ),
    ]
