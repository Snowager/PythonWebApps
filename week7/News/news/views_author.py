from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Author


class AuthorView(RedirectView):
    url = reverse_lazy('author_list')


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     kwargs.update(dict(dependent=Dependent.obects.filter(author=kwargs.get('object'))))
    #     return kwargs


class AuthorCreateView(LoginRequiredMixin, CreateView):
    template_name = "author_add.html"
    model = Author
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = 1
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = '__all__'


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')
