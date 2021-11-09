from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, TextField
from django_mysql.models import ListCharField



class User(AbstractUser):
    age = models.IntegerField(null=True)

class Sleep(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateField()
    total_time = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '睡眠'
        verbose_name_plural = '睡眠'

class Breakfast(models.Model):
    STATUS_CHOICES = [(1, '食べてない'),(2, '食べた')]
    date = models.DateTimeField(auto_now_add=True)
    menu = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '朝食'
        verbose_name_plural = '朝食'

class Cleaning(models.Model):
    STATUS_CHOICES = [(1, '掃除してない'),(2, '掃除した')]
    date = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
    place = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '掃除'
        verbose_name_plural = '掃除'

class Exercise(models.Model):
    STATUS_CHOICES = [(1, '運動してない'),(2, '運動した')]
    date = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
    genre = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '運動'
        verbose_name_plural = '運動'

class Todo(models.Model):
    STATUS_CHOICES = [(1, '未'),(2, '作業中'),(3, '済')]
    date = models.DateTimeField(auto_now_add=True)
    task = CharField(max_length=250)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    finish_task  = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'

class Diary(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = TextField(max_length=15000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '日記'
        verbose_name_plural = '日記'

class Condition(models.Model):
    STATUS_CHOICES = [(1, '調子が悪い'),(2, '普通'),(3, '調子が良い')]
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '体調'
        verbose_name_plural = '体調'

class SleepAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    ave_start_time = models.DateTimeField()
    fastest_start_time = models.DateTimeField()
    lateest_start_time = models.DateTimeField()
    ave_end_time = models.DateField()
    fastest_end_time = models.DateField()
    lateest_end_time = models.DateField()
    ave_total_time = models.IntegerField()
    fastest_total_time = models.IntegerField()
    lateest_total_time = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '睡眠分析'
        verbose_name_plural = '睡眠分析'

class BreakfastAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    total_meal_days = models.CharField(max_length=250)
    menu_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '朝食分析'
        verbose_name_plural = '朝食分析'

class CleaningAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    total_cleaning_days = models.CharField(max_length=250)
    total_cleaning_time = models.IntegerField()
    ave_cleaning_time = models.IntegerField()
    max_cleaning_time = models.IntegerField()
    min_cleaning_time = models.IntegerField()
    place_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '掃除分析'
        verbose_name_plural = '掃除分析'

class ExerciseAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    total_exrcise_days = models.CharField(max_length=250)
    total_exrcise_time = models.IntegerField()
    ave_exrcise_time = models.IntegerField()
    max_exrcise_time = models.IntegerField()
    min_exrcise_time = models.IntegerField()
    exercise_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '運動分析'
        verbose_name_plural = '運動朝食分析'


class TodoAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    ave_task_progress = models.IntegerField()
    total_task_time = models.IntegerField()
    ave_task_time = models.IntegerField()
    max_task_time = models.IntegerField()
    min_task_time = models.IntegerField()
    finish_task_list = ListCharField(
        models.CharField(max_length=100),size=6, max_length=(1000))
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo分析'
        verbose_name_plural = 'Todo分析'

class ConditionAnalysis(models.Model):
    period = models.DateTimeField(auto_now_add=False)
    ave_condition = models.IntegerField()
    total_fine_conditon = models.IntegerField()
    total_normal_conditon = models.IntegerField()
    total_bad_conditon = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name = '体調分析'
        verbose_name_plural = '体調分析'