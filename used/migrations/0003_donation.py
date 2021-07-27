# Generated by Django 3.2.4 on 2021-07-27 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('used', '0002_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('phone_number', models.SmallIntegerField()),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=64)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.DateField()),
                ('pick_up_comment', models.CharField(max_length=150)),
                ('categories', models.ManyToManyField(to='used.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='used.institution')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
