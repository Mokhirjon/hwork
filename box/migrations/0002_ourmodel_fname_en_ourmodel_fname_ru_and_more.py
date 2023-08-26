# Generated by Django 4.2.4 on 2023-08-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourmodel',
            name='fname_en',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='fname_ru',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='fname_uz',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='name_en',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='name_ru',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='name_uz',
            field=models.CharField(default='', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='text_en',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='text_ru',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='ourmodel',
            name='text_uz',
            field=models.TextField(default='', null=True),
        ),
        migrations.DeleteModel(
            name='ModelWithTranslator',
        ),
    ]