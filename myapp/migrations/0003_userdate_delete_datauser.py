# Generated by Django 4.2.7 on 2024-01-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_datauser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('cameracompany', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('range', models.IntegerField(default=0, null=True)),
                ('location', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(default=0, null=True)),
                ('mobile', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='DataUser',
        ),
    ]
