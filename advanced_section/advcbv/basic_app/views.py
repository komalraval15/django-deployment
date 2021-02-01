from django.shortcuts import render,HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView 
from .models import School
from django.urls import reverse_lazy
                            
from . import models



class IndexView(TemplateView):
    template_name = 'index.html'
#     def get_context_data(self,**kwargs):
#         context =   super().get_context_data(**kwargs)
#         context['injectme'] = "BASE INJECTTION!!!!!"
#         return context
    
class SchoolListView(ListView):
    #return schoollist
    # context_object_name = 'schools'
    model = School
    # queryset = models.School.objects.all()
    # template_name = "school_list.html"
    def get_context_data(self, **kwargs):
        print("Hello")
        context = super().get_context_data(**kwargs)
        return context

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    # queryset = School.objects.all()
    # print(queryset)
    template_name = 'basic_app/school_detail.html'
  


class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')