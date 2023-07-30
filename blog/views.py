from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        article_formset = modelformset_factory(Article, form=ArticleForm, extra=1)
        context_data['title'] = 'Добавить товар'
        if self.request.method == 'POST':
            context_data['formset'] = article_formset(self.request.POST)
        else:
            context_data['formset'] = article_formset()
        return context_data

    def form_valid(self, form):
        mailing = form.save()
        mailing.user = self.request.user
        mailing.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        article_formset = modelformset_factory(Article, form=ArticleForm, extra=1)
        context_data['title'] = 'Добавить товар'
        if self.request.method == 'POST':
            context_data['formset'] = article_formset(self.request.POST)
        else:
            context_data['formset'] = article_formset()
        return context_data


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    permission_required = 'blog.delete_article'
    success_url = reverse_lazy('blog:article_list')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
