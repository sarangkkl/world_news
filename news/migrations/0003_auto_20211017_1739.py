# Generated by Django 3.2.8 on 2021-10-17 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_delete_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
        migrations.AddField(
            model_name='news',
            name='main_image_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_keyword',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_title',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('body', models.TextField(blank=True, max_length=5000, null=True)),
                ('emal', models.CharField(blank=True, max_length=100, null=True)),
                ('belong_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
        ),
    ]
