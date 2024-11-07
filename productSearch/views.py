from django.http import HttpResponse, HttpResponseNotFound
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer 

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

def index(request):
    return HttpResponse("main index")

def error_404_view(request, exception):
    return HttpResponseNotFound("404 error")


# create a mehtod that will get the product name and return the product details from elastic search
def get_product(request, _id):
    # If the product name is not provided, return an error message
    if _id is None:
        return HttpResponse("Please provide a product name")
    
    # Search for the product in Elasticsearch
    response = es.search(index="product", body={
        "query": {
            "ids": {
                "values": [_id]
            }
        }
    })
    
    # If no product is found, return an error message
    if not response['hits']['hits']:
        return HttpResponse("Product not found")
    
    # If the product is found, return the product details
    product_details = response['hits']['hits'][0]['_source']
    return HttpResponse(f"Product details: {product_details}")


                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                    