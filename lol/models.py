# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'exams'
        verbose_name = _('exam')
        verbose_name_plural = _('exams')
        ordering = ('id',) 

    def __unicode__(self):
        return str(self.name)


class ExamRegistrtion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    mobile = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)
    register_number = models.CharField(max_length=128)
    auto_id = models.PositiveIntegerField()
    age = models.CharField(max_length=128)

    class Meta:
        db_table = 'exam_registration'
        verbose_name = _('registration')
        verbose_name_plural = _('registrations')

    def __unicode__(self):
        return str(self.name)
    
