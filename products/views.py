# products/views.py
from django.shortcuts import render
from .models import Product
from .documents import ProductDocument
from elasticsearch_dsl import connections

# Establish Elasticsearch connection
# connections.create_connection(alias='default', hosts=['localhost:9200'])

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def search_products(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = ProductDocument.search().query("multi_match", query=query, fields=['name', 'description'])
    return render(request, 'products/search.html', {'results': results, 'query': query})
