# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    label = models.CharField(verbose_name="Label", max_length=15)
    def __unicode__(self):
        return "{0}".format(self.label)
    class Meta:
        verbose_name = "Categorie"

class Post(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=30)
    slug = AutoSlugField(populate_from='title', editable=True)
    body = models.TextField(verbose_name="Contenu", blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Article"
