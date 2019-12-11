from django.db import models
from django.utils.translation import ugettext_lazy as _


class Document(models.Model):
    name = models.CharField(verbose_name=_('Name'), null=False, max_length=500)

    class Meta:
        db_table = 'documents'
        managed = True
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')


class URL(models.Model):
    link = models.URLField(verbose_name=_('Link'), null=False, max_length=500)
    active = models.BooleanField(verbose_name=_('Active'))
    document = models.ForeignKey(
        to='Document',
        verbose_name=_('Documents'),
        related_name='links',
        related_query_name='links',
        on_delete=models.CASCADE,
        null=True,
        default=None
    )

    class Meta:
        db_table = 'links'
        managed = True
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
