# Generated by Django 3.2.8 on 2021-10-12 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TischtennisAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainingsplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='ttuser',
            name='id',
        ),
        migrations.AddField(
            model_name='ttuser',
            name='spielstil',
            field=models.CharField(default='shakehand', max_length=30),
        ),
        migrations.AddField(
            model_name='ttuser',
            name='ttrpunkte',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='ttuser',
            name='verein',
            field=models.CharField(default='nicht angegeben', max_length=100),
        ),
        migrations.AlterField(
            model_name='ttuser',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Übungen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('komplexität', models.CharField(max_length=50)),
                ('intensität', models.CharField(max_length=50)),
                ('trainingsplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TischtennisAPP.trainingsplan')),
            ],
        ),
        migrations.AddField(
            model_name='trainingsplan',
            name='ttuser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TischtennisAPP.ttuser'),
        ),
    ]