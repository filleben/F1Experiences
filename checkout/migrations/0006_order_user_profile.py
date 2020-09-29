# Generated by Django 3.0.8 on 2020-09-29 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('checkout', '0005_auto_20200929_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='accounts.UserProfile'),
        ),
    ]