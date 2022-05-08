# Generated by Django 3.1.14 on 2022-05-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientLeads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('product', models.CharField(choices=[('1', 'PR1'), ('2', 'PR2'), ('3', 'PR3'), ('4', 'PR4'), ('5', 'PR5')], max_length=1)),
                ('location', models.CharField(max_length=70)),
            ],
        ),
    ]