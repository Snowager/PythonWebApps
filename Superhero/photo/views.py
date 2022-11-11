from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
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

class PhotoCarouselView(TemplateView):
    template_name = 'photo/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Image.objects.all()
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)


def carousel_data(photos):

    def photo_data(id, image, url):
        x = dict(image_url=url, id=str(id), label=f"{image} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x

    return [photo_data(id, photo.image, photo.image.url) for id, photo in enumerate(photos)]

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


