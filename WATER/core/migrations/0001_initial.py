# Generated by Django 4.1 on 2022-08-26 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(default=10)),
                ('maker', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('expired', models.BooleanField(default=True)),
                ('orders', models.ManyToManyField(blank=True, related_name='bottles', to='clients.order', verbose_name='Orders')),
            ],
        ),
        migrations.CreateModel(
            name='BottlesCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('bottle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottle_count', to='core.bottle')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='clients.order')),
            ],
        ),
    ]