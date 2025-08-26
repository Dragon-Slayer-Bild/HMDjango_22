from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "description", "preview", "publication"]
    success_url = reverse_lazy("blog:blog_list")


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        # Получаем все статьи
        queryset = super().get_queryset()

        # Фильтруем статьи
        return queryset.filter(publication=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        # Получаем объект статьи
        obj = super().get_object(queryset)

        obj.views += 1
        obj.save()  # Сохраняем изменения в базе данных

        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "description", "preview", "publication"]
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
