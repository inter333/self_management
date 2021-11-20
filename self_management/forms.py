from django import forms
from . import models

class SleepForm(forms.ModelForm):
    class Meta:
        model = models.Sleep
        fields = ("start_time","end_time","total_time",)
        labels = [
            {"start_time":"就寝時間"},
            {"end_time":"起床時間"},
            {"total_time":"合計時間"},
        ]

class BreakfastForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(BreakfastForm, self).__init__(*args, **kwd)
        self.fields["menu"].required = False
    class Meta:
        model = models.Breakfast
        fields = ("status","menu",)
        labels = [
            {"status":"朝食食べた？"},
            {"menu":"朝食のメニュー"},
        ]

class CleaningForm(forms.ModelForm):
    class Meta:
        model = models.Cleaning
        fields = ("status","place","time",)
        labels = [
            {"status":"掃除した？"},
            {"place":"掃除した場所"},
            {"time":"掃除時間"},
        ]

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = models.Exercise
        fields = ("status","genre","time",)
        labels = [
            {"status":"運動した？"},
            {"genre":"何の運動？"},
            {"time":"運動時間"},
        ]

class MorningTodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ("task",)
        labels = [
            {"task":"タスク"},
        ]
class NightTodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ("status","finish_task",)
        labels = [
            {"status":"タスクの状態"},
            {"finish_task":"終わったタスク"},
        ]

class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ("content",)
        labels = [
            {"content":"日記"},
        ]
class ConditionForm(forms.ModelForm):
    class Meta:
        model = models.Condition
        fields = ("status",)
        labels = [
            {"condition":"体調・気分の良し悪し"},
        ]