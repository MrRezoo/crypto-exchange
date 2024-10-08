# Generated by Django 5.1.1 on 2024-10-09 08:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exchanges', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('amount', models.DecimalField(decimal_places=8, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING', max_length=10)),
                ('is_aggregated', models.BooleanField(default=False)),
                ('crypto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exchanges.cryptocurrency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['is_aggregated'], name='orders_orde_is_aggr_462bec_idx'), models.Index(fields=['state'], name='orders_orde_state_d5ccd0_idx')],
            },
        ),
    ]
