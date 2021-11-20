from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, TextField
from django_mysql.models import ListCharField
from django.contrib.auth import get_user_model



class User(AbstractUser):
    age = models.IntegerField(null=True)

class Sleep(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_time = models.FloatField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '睡眠'
        verbose_name_plural = '睡眠'

class Breakfast(models.Model):
    STATUS_CHOICES = [(1, '食べてない'),(2, '食べた')]
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    menu = ListCharField(
        models.CharField(max_length=100,blank=True),size=6, max_length=(1000))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '朝食'
        verbose_name_plural = '朝食'

class Cleaning(models.Model):
    STATUS_CHOICES = [(1, '掃除してない'),(2, '掃除した')]
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.FloatField()
    place = ListCharField(
        models.CharField(max_length=100,blank=True),size=6, max_length=(1000))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '掃除'
        verbose_name_plural = '掃除'

class Exercise(models.Model):
    STATUS_CHOICES = [(1, '運動してない'),(2, '運動した')]
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.FloatField()
    genre = ListCharField(
        models.CharField(max_length=100,blank=True),size=6, max_length=(1000))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '運動'
        verbose_name_plural = '運動'

class Todo(models.Model):
    STATUS_CHOICES = [(1, '未'),(2, '作業中'),(3, '済')]
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    task = CharField(max_length=250)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    finish_task  = ListCharField(
        models.CharField(max_length=100,blank=True),size=6, max_length=(1000))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    flg = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'

class Diary(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    content = TextField(max_length=15000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '日記'
        verbose_name_plural = '日記'

class Condition(models.Model):
    STATUS_CHOICES = [(1, '調子が悪い'),(2, '普通'),(3, '調子が良い')]
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '体調'
        verbose_name_plural = '体調'

class SleepAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    ave_start_time = models.DateTimeField()
    fastest_start_time = models.TimeField()
    lateest_start_time = models.TimeField()
    ave_end_time = models.TimeField()
    fastest_end_time = models.TimeField()
    lateest_end_time = models.TimeField()
    ave_total_time = models.FloatField()
    fastest_total_time = models.FloatField()
    lateest_total_time = models.FloatField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '睡眠分析'
        verbose_name_plural = '睡眠分析'

class BreakfastAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    total_meal_days = models.CharField(max_length=250)
    menu_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '朝食分析'
        verbose_name_plural = '朝食分析'

class CleaningAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    total_cleaning_days = models.CharField(max_length=250)
    total_cleaning_time = models.FloatField()
    ave_cleaning_time = models.FloatField()
    max_cleaning_time = models.FloatField()
    min_cleaning_time = models.FloatField()
    place_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '掃除分析'
        verbose_name_plural = '掃除分析'

class ExerciseAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    total_exrcise_days = models.CharField(max_length=250)
    total_exrcise_time = models.FloatField()
    ave_exrcise_time = models.FloatField()
    max_exrcise_time = models.FloatField()
    min_exrcise_time = models.FloatField()
    exercise_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '運動分析'
        verbose_name_plural = '運動朝食分析'


class TodoAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    ave_task_progress = models.FloatField()
    total_task_time = models.FloatField()
    ave_task_time = models.FloatField()
    max_task_time = models.FloatField()
    min_task_time = models.FloatField()
    finish_task_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo分析'
        verbose_name_plural = 'Todo分析'

class ConditionAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    ave_condition = models.FloatField()
    total_fine_conditon = models.IntegerField()
    total_normal_conditon = models.IntegerField()
    total_bad_conditon = models.IntegerField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '体調分析'
        verbose_name_plural = '体調分析'