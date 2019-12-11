from django.contrib import admin

from pdfscrapper.apps.documents.models import Document, URL

admin.site.register(Document)
admin.site.register(URL)
