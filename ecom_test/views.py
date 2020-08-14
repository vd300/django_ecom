from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Product


def home(requset):
    context = {
        'products': Product.objects.all()
    }
    return render(requset, 'ecom_test/home.html', context)


def about(request):
    return HttpResponse('<h1>About Page</h1>')


class ProdListView(ListView):
    model = Product
    template_name = 'ecom_test/home.html'
    context_object_name = 'products'
    ordering = ['-date_posted']


class ProdDetailView(DetailView):
    model = Product


class ProdCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_title', 'product_desc', 'product_price', 'product_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['product_title', 'product_desc', 'product_price', 'product_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


class ProdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = "/"

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False
