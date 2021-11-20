from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,FormView
from django.http import HttpResponse
from django.db import transaction
from .forms import *
from .models import Todo
import datetime

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'self_management/index.html'

class CreateMoringView(FormView):
    form_class =SleepForm
    form_class2 =BreakfastForm
    form_class3 = MorningTodoForm
    template_name = 'self_management/create_morning.html'

    def get_context_data(self, **kwargs):
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        obj = Todo.objects.filter(flg = 0,date__range=(yesterday, datetime.datetime.now()))

        context= CreateView.get_context_data(self, **kwargs)
        form2 = self.form_class2(self.request.GET or None)
        form3 = self.form_class3(self.request.GET or None)
        context.update({'form2':form2,'form3':form3})
        return context

    def form_valid(self, form):
        form2 = self.form_class2(self.request.POST or None)
        form3 = self.form_class3(self.request.POST or None)
        if (form2.is_valid()) and (form3.is_valid()):
            with transaction.atomic():
                qryset =  form.save(commit=False)
                print(qryset.start_time)
                qryset2 =  form2.save(commit=False)
                qryset3 =  form3.save(commit=False)
                qryset.author=self.request.user
                qryset2.author=self.request.user
                qryset3.author=self.request.user
                qryset.save()
                qryset2.save()
                qryset3.save()
        return HttpResponse('FormValid')

class CreateNightView(FormView):
    form_class =CleaningForm
    form_class2 =ExerciseForm
    form_class3 = NightTodoForm
    form_class4 = DiaryForm
    form_class5 = ConditionForm

    template_name = 'self_management/create_night.html'

    def get_context_data(self, **kwargs):
       context= CreateView.get_context_data(self, **kwargs)
       form2 = self.form_class2(self.request.GET or None)
       form3 = self.form_class3(self.request.GET or None)
       form4 = self.form_class4(self.request.GET or None)
       form5 = self.form_class5(self.request.GET or None)
       context.update({'form2':form2,'form3':form3,'form4':form4,'form5':form5})
       return context

    def form_valid(self, form):
        form2 = self.form_class2(self.request.POST or None)
        form3 = self.form_class3(self.request.POST or None)
        form4 = self.form_class4(self.request.POST or None)
        form5 = self.form_class5(self.request.POST or None)
        if (form2.is_valid()) and (form3.is_valid()) and (form4.is_valid()) and (form5.is_valid()):
            with transaction.atomic():
                qryset =  form.save(commit=False)
                qryset2 =  form2.save(commit=False)
                qryset3 =  form3.save(commit=False)
                qryset4 =  form4.save(commit=False)
                qryset5 =  form5.save(commit=False)
                qryset.author=self.request.user
                qryset2.author=self.request.user
                qryset3.author=self.request.user
                qryset4.author=self.request.user
                qryset5.author=self.request.user
                qryset.save()
                qryset2.save()
                qryset3.save()
                qryset4.save()
                qryset5.save()
        return HttpResponse('FormValid')

def check_morning(self):
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    obj = Todo.objects.filter(flg = 0,date__range=(yesterday, today))
