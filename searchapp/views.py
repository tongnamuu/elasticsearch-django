from django.shortcuts import render
from django.http import JsonResponse
from .elasticsearch_client import create_index, add_document

def create_index_view(request):
    index_name = 'my_index'
    create_index(index_name)
    return JsonResponse({'status': 'Index created'})

def add_document_view(request):
    index_name = 'my_index'
    doc_type = '_doc'
    document = {
        'title': 'Sample Document',
        'content': 'This is a sample document for Elasticsearch.'
    }
    add_document(index_name, doc_type, document)
    return JsonResponse({'status': 'Document added'})

