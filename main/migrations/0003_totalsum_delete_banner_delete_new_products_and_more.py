# Generated by Django 5.0.2 on 2024-03-18 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.TextField()),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total_expenses', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='New_Products',
        ),
        migrations.DeleteModel(
            name='Shop_colloection',
        ),
        migrations.DeleteModel(
            name='Treding_ats',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='totalsum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]