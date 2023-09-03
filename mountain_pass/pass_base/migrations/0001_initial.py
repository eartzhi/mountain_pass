# Generated by Django 4.2.4 on 2023-09-03 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('fam', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('otc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=8)),
                ('longitude', models.FloatField(max_length=8)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('NI', 'нет информации'), ('A1', '1А'), ('B1', '1Б'), ('А2', '2А'), ('В2', '2Б'), ('А3', '3А'), ('В3', '3Б')], default='NI', max_length=2)),
                ('summer', models.CharField(choices=[('NI', 'нет информации'), ('A1', '1А'), ('B1', '1Б'), ('А2', '2А'), ('В2', '2Б'), ('А3', '3А'), ('В3', '3Б')], default='NI', max_length=2)),
                ('autumn', models.CharField(choices=[('NI', 'нет информации'), ('A1', '1А'), ('B1', '1Б'), ('А2', '2А'), ('В2', '2Б'), ('А3', '3А'), ('В3', '3Б')], default='NI', max_length=2)),
                ('spring', models.CharField(choices=[('NI', 'нет информации'), ('A1', '1А'), ('B1', '1Б'), ('А2', '2А'), ('В2', '2Б'), ('А3', '3А'), ('В3', '3Б')], default='NI', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_image_name', models.TextField()),
                ('per_image', models.ImageField(blank=True, upload_to='Pass_images', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(choices=[('NI', 'нет информации'), ('PS', 'Перевал'), ('TP', 'Вершина'), ('GL', 'Ледник'), ('IO', 'Объект инфраструктуры'), ('NO', 'Объект природы')], default='NI', max_length=2)),
                ('title', models.TextField()),
                ('other_titles', models.TextField()),
                ('connect', models.TextField(default='')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NEW', 'новый'), ('PEN', 'в работе'), ('ACC', 'принят'), ('REJ', 'отклонен')], default='NEW', max_length=3)),
                ('spr_activities_types', models.CharField(choices=[('1', 'пешком'), ('2', 'лыжи'), ('3', 'катамаран'), ('4', 'байдарка'), ('5', 'плот'), ('6', 'сплав'), ('7', 'велосипед'), ('8', 'автомобиль'), ('9', 'мотоцикл'), ('10', 'парус'), ('11', 'верхом')], default='1', max_length=2)),
                ('add_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_base.perevalimages')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_base.author')),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_base.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_base.level')),
            ],
        ),
    ]