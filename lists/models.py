from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owners_lists', blank=True, null=True)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='lists_shared_with', blank=True)

    @property
    def name(self):
        return self.item_set.first().text

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(list=list_, text=first_item_text)
        return list_


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        unique_together=('list', 'text')

    def __str__(self):
        return self.text
