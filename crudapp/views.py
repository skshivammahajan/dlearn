# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crudapp.forms import EmployeeForm
from crudapp.models import BlogPost , Employee


class PostsForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'tag', 'author']


def post_list(request):
    posts = BlogPost.objects.all()
    data = {'object_list': posts}
    return render(request, 'blog_posts/post_list.html', data)


def post_create(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crudapp:post_list')
    return render(request, 'blog_posts/post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, 'blog_posts/post_form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('crudapp:post_list')
    return render(request, 'blog_posts/post_delete.html', {'object': post})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('crudapp:emp_show')
            except Exception:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'employee/show.html', {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("crudapp:emp_show")
    return render(request, 'employee/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("crudapp:emp_show")

