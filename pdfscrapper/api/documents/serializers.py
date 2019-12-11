from rest_framework import serializers

from pdfscrapper.apps.documents.models import Document, URL


class DocumentSerializer(serializers.ModelSerializer):
    # urls_count = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = '__all__'

    def get_urls_count(self, obj):
        return len(list(URL.objects.filter(document_id=obj.id)))


class URLSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = ('link', 'active', )


class PDFUploadSerializer(serializers.Serializer):
    pdf = serializers.FileField(required=True)
