# Generated by Django 4.2.1 on 2023-05-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='collegeList',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('outputSS', models.FileField(upload_to='media-root/college_img')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('crid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TreandingProjects',
            fields=[
                ('tpid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('frontimg', models.FileField(upload_to='media-root/treandingProject')),
            ],
        ),
        migrations.CreateModel(
            name='uploadProject',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=80)),
                ('fname', models.CharField(max_length=220)),
                ('lname', models.CharField(max_length=220)),
                ('email', models.CharField(max_length=220)),
                ('College', models.TextField()),
                ('course', models.TextField()),
                ('projectname', models.CharField(max_length=220)),
                ('tags', models.TextField()),
                ('description', models.TextField()),
                ('zip_project', models.FileField(upload_to='media-root/zip_projects')),
                ('outputSS', models.FileField(upload_to='media-root/outputSS')),
            ],
        ),
    ]