# Generated by Django 4.2.4 on 2023-09-04 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pass_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='pass_base.pereval', verbose_name='перевал'),
        ),
    ]
