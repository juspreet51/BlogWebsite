# Generated by Django 4.1 on 2023-01-24 06:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('query', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeline', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='project/')),
                ('github_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='cat',
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='personal/')),
                ('email', models.EmailField(max_length=254)),
                ('github', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
                ('twitter', models.CharField(default='', max_length=200)),
                ('youtube', models.CharField(default='', max_length=200)),
                ('phone', models.IntegerField()),
                ('resume', models.FileField(default='settings.MEDIA_ROOT/resume/resume.pdf', upload_to='resume/')),
                ('year_experience', models.IntegerField(default=0)),
                ('project_completed', models.IntegerField(default=0)),
                ('happy_client', models.IntegerField(default=0)),
                ('customer_review', models.IntegerField(default=12)),
                ('experience', models.ManyToManyField(to='home.experience')),
                ('project', models.ManyToManyField(to='home.project')),
                ('skills', models.ManyToManyField(to='home.skills')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='cat',
            field=models.ManyToManyField(to='home.category'),
        ),
    ]
