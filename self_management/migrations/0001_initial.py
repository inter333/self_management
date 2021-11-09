# Generated by Django 3.2.8 on 2021-11-08 14:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TodoAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField()),
                ('ave_task_progress', models.IntegerField()),
                ('total_task_time', models.IntegerField()),
                ('ave_task_time', models.IntegerField()),
                ('max_task_time', models.IntegerField()),
                ('min_task_time', models.IntegerField()),
                ('finish_task_list', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Todo分析',
                'verbose_name_plural': 'Todo分析',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('task', models.CharField(max_length=250)),
                ('status', models.IntegerField(choices=[(1, '未'), (2, '作業中'), (3, '済')], default=1)),
                ('finish_task', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todo',
            },
        ),
        migrations.CreateModel(
            name='SleepAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField()),
                ('ave_start_time', models.DateTimeField()),
                ('fastest_start_time', models.DateTimeField()),
                ('lateest_start_time', models.DateTimeField()),
                ('ave_end_time', models.DateField()),
                ('fastest_end_time', models.DateField()),
                ('lateest_end_time', models.DateField()),
                ('ave_total_time', models.IntegerField()),
                ('fastest_total_time', models.IntegerField()),
                ('lateest_total_time', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '睡眠分析',
                'verbose_name_plural': '睡眠分析',
            },
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateField()),
                ('total_time', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '睡眠',
                'verbose_name_plural': '睡眠',
            },
        ),
        migrations.CreateModel(
            name='ExerciseAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField()),
                ('total_exrcise_days', models.CharField(max_length=250)),
                ('total_exrcise_time', models.IntegerField()),
                ('ave_exrcise_time', models.IntegerField()),
                ('max_exrcise_time', models.IntegerField()),
                ('min_exrcise_time', models.IntegerField()),
                ('exercise_list', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '運動分析',
                'verbose_name_plural': '運動朝食分析',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.IntegerField()),
                ('genre', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('status', models.IntegerField(choices=[(1, '運動してない'), (2, '運動した')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '運動',
                'verbose_name_plural': '運動',
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=15000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '日記',
                'verbose_name_plural': '日記',
            },
        ),
        migrations.CreateModel(
            name='ConditionAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField()),
                ('ave_condition', models.IntegerField()),
                ('total_fine_conditon', models.IntegerField()),
                ('total_normal_conditon', models.IntegerField()),
                ('total_bad_conditon', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '体調分析',
                'verbose_name_plural': '体調分析',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, '調子が悪い'), (2, '普通'), (3, '調子が良い')], default=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '体調',
                'verbose_name_plural': '体調',
            },
        ),
        migrations.CreateModel(
            name='CleaningAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField()),
                ('total_cleaning_days', models.CharField(max_length=250)),
                ('total_cleaning_time', models.IntegerField()),
                ('ave_cleaning_time', models.IntegerField()),
                ('max_cleaning_time', models.IntegerField()),
                ('min_cleaning_time', models.IntegerField()),
                ('place_list', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '掃除分析',
                'verbose_name_plural': '掃除分析',
            },
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.IntegerField()),
                ('place', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('status', models.IntegerField(choices=[(1, '掃除してない'), (2, '掃除した')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '掃除',
                'verbose_name_plural': '掃除',
            },
        ),
        migrations.CreateModel(
            name='BreakfastAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField()),
                ('total_meal_days', models.CharField(max_length=250)),
                ('menu_list', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '朝食分析',
                'verbose_name_plural': '朝食分析',
            },
        ),
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('menu', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=1000, size=6)),
                ('status', models.IntegerField(choices=[(1, '食べてない'), (2, '食べた')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '朝食',
                'verbose_name_plural': '朝食',
            },
        ),
    ]