from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User,Group
from django.forms.models import ModelForm
from django import forms
from django.template.defaultfilters import slugify
import string, datetime


class List(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60,editable=False)
    
    group = models.ForeignKey(Group)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(List, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    # Custom manager - can complete all for example
    objects = models.Manager()

    def incomplete_tasks(self):
        # Counts all incomplete tasks in current list instance
        return Item.objects.filter(list=self,completed=0)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Lists"
        
        # At the db, prevents creation of lists with same name and group
        unique_together = ("group", "slug")

class Item(models.Model):
    title = models.CharField(max_length=140)
    list = models.ForeignKey(List)
    created_date = models.DateField(auto_now=True, auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField()
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="created_by")
    assigned_to = models.ForeignKey(User, related_name="bug_assigned_to")
    note = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(max_length=3)

    # model method: checks due date with current date to see if passed
    def overdue_status(self):
        if datetime.date.today() > self.due_date :
            return 1
            
    def __unicode__(self):
        return self.title
        
    # completed date
    def save(self):
        if self.completed :
            self.completed_date = datetime.datetime.now()
        super(Item,self).save()

    class Meta:
        ordering = ["priority"]

class Comment(models.Model):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Item)
    date = models.DateTimeField(default=datetime.datetime.now)
    body = models.TextField(blank=True)

    def __unicode__(self):
        return '%s - %s' % (
            self.author,
            self.date,
            )
