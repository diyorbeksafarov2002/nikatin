# Generated by Django 5.0.2 on 2024-02-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=13)),
                ('called', models.CharField(choices=[("Bog'lanildi", 'Boglanildi'), ("Bog'lanilmadi", 'Boglanilmadi')], default="Bog'lanilmadi", max_length=100)),
            ],
        ),
    ]
