from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image

class PhotoListView(ListView):
    template_name =  "photo/list.html"
    model = Image
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    template_name = "photo/detail.html"
    model = Image
    context_object_name = "photo"

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo/add.html'
    model = Image
    fields = '__all__'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('photo_list')

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'photo/edit.html'
    model = Image
    fields = '__all__'

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'photo/delete.html'
    model = Image
    success_url = reverse_lazy('photo_list')


