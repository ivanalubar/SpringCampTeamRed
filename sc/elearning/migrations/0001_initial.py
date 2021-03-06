from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(default='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('duration', models.IntegerField(default=0)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('number_of_people', models.IntegerField(default=0, null=True)),
                ('description', models.CharField(default='', max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area', to='auth.Group')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='NasUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UserIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('course_list', models.ManyToManyField(blank=True, null=True, to='elearning.Course')),

                ('phone', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='programmes',
            field=models.ManyToManyField(blank=True, null=True, to='elearning.Program'),
        ),
    ]
