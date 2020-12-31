from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
