#!coding:utf8
# create by  @
from django.db import models
from uuid import uuid1
from lebang_vote.user.models import Voter


class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Game(Base):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=1024*10)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.IntegerField(default=0)  # online / offline
    image = models.CharField(max_length=1024, default='', blank=True)  # head image
    title = models.CharField(max_length=1024)  # display title
    sub_title = models.CharField(max_length=1024, default="", blank=True)
    max_vote = models.IntegerField(default=1)  # 最多
    voted_person = models.IntegerField(default=0)  # 人数
    visted = models.IntegerField(default=0)
    voted_amount = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s_%s" % (self.name, self.title)


class Option(Base):
    game = models.ForeignKey(Game, related_name='options')
    title = models.CharField(max_length=1024)
    content = models.CharField(max_length=1024*10)
    image_url = models.CharField(max_length=1024, default='', blank=True)
    count_vote = models.IntegerField(default=0)
    count_visit = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s_%s" % (self.game.name, self.title)


class VoteLog(Base):
    voter = models.ForeignKey(Voter)
    option = models.ForeignKey(Option)
    value = models.IntegerField(default=1)


class Counter(Base):
    value = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default="")

    def __uuid__(self):
        return "%s_%s" % (self.__class__.name, self.pk)