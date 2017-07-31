# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length = 30, unique = True)
    def __str__(self):
        return self.name.encode('utf-8')




class Good(models.Model):
    name =  models.CharField(max_length =50, unique = True)
    description =  models.TextField()
    in_stock = models.BooleanField(default =  True, db_index = True)
    category =  models.ForeignKey(Category, null= True, blank = True, on_delete = models.SET_NULL)
    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (няма у наяунасьцi)"
        return s.encode('utf-8')
        
    def get_is_stock(self):
        if self.in__stock:
          return "+"
        else:
          return ""    

    """class  Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары" """