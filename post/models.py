# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=30)
    body = models.TextField(verbose_name="Contenu", blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name="Slug")

    def __unicode__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Article"
