from django.conf.urls import url

from pdfscrapper.api.documents.views import AllDocumentsView, AllURLsView, \
    URLByDocumentIdView, UploadPDFView

urlpatterns = [
    url(r'^documents/?$', AllDocumentsView.as_view()),
    url(r'^documents/(?P<document_id>[0-9]*)/links/?$',
        URLByDocumentIdView.as_view()),
    url(r'^documents/upload/?$', UploadPDFView.as_view()),
    url(r'^links/?$', AllURLsView.as_view())
]
