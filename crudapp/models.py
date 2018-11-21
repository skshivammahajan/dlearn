# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"
