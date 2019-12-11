from collections import Counter

from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pdfscrapper.apps.documents.checker import check_url_alive
from pdfscrapper.apps.documents.models import Document, URL
from pdfscrapper.apps.documents.pdf_parser import extract_hyperlinks
from pdfscrapper.api.documents.serializers import DocumentSerializer, \
    URLSerializer, PDFUploadSerializer


class URLByDocumentIdView(APIView):
    http_method_names = ['get', ]

    def get(self, request, document_id):
        urls = get_list_or_404(URL, document_id=document_id)
        serializer = URLSerializer(urls, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AllURLsView(APIView):
    http_method_names = ['get', ]

    def get(self, request):
        links = [url.link for url in URL.objects.all()]
        return Response(data=dict(Counter(links)), status=status.HTTP_200_OK)


class AllDocumentsView(APIView):
    http_method_names = ['get', ]

    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UploadPDFView(APIView):
    http_method_names = ['post', ]

    def post(self, request):
        serializer = PDFUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pdf_file = serializer.validated_data['pdf']
        links = extract_hyperlinks(pdf_file)

        document = Document.objects.create(name=pdf_file.name)
        db_links = [URL(link=link, active=check_url_alive(link),
                        document=document) for link in links]
        URL.objects.bulk_create(db_links)

        return Response(status=status.HTTP_201_CREATED)
