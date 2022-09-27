# Generated by Django 4.0.6 on 2022-09-17 04:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('o_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('o_date', models.DateTimeField()),
                ('o_status', models.CharField(max_length=10)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('rt_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('rt_name', models.CharField(max_length=255)),
                ('rt_price', models.IntegerField(default=0)),
                ('rt_limit', models.IntegerField(default=2)),
                ('rt_image', models.TextField(blank=True, null=True)),
                ('rt_description', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('lineid', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=30, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('ewallet', models.TextField(blank=True, null=True)),
                ('einvoice', models.CharField(blank=True, max_length=20, null=True)),
                ('GUInumber', models.CharField(blank=True, max_length=20, null=True)),
                ('followdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_number', models.TextField()),
                ('t_amount', models.IntegerField(default=0)),
                ('t_method', models.CharField(max_length=50)),
                ('t_date', models.DateTimeField()),
                ('t_status', models.BooleanField(default=False)),
                ('t_invoice_type', models.CharField(max_length=50, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.order')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('r_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('room_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.roomtype')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.roomtype'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.users'),
        ),
        migrations.CreateModel(
            name='BookingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_date', models.DateTimeField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.order')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.room')),
            ],
        ),
    ]
