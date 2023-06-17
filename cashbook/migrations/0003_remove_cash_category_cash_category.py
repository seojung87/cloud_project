# Generated by Django 4.2.2 on 2023-06-17 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashbook', '0002_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cash',
            name='category',
        ),
        migrations.AddField(
            model_name='cash',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='cashbook.category'),
            preserve_default=False,
        ),
    ]