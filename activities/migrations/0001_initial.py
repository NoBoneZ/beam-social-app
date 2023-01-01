# Generated by Django 4.1 on 2022-09-16 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('location', models.CharField(max_length=100, null=True)),
                ('is_started', models.BooleanField(default=False)),
                ('yes', models.JSONField(blank=True, default=list, null=True)),
                ('no', models.JSONField(blank=True, default=list, null=True)),
                ('maybe', models.JSONField(blank=True, default=list, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Kindly input the question', max_length=90, null=True)),
                ('description', models.CharField(max_length=500)),
                ('start_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField()),
                ('poll_option', models.JSONField(default=dict, help_text='Maximum of 4 Options')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('is_admin_notification', models.BooleanField(default=False)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group')),
                ('user', models.ManyToManyField(related_name='notification_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-time_stamp',),
            },
        ),
        migrations.CreateModel(
            name='EventInvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.members')),
            ],
        ),
    ]