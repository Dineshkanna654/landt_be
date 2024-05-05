from django.http import JsonResponse
from collections import defaultdict
from rest_framework.decorators import api_view
import json

@api_view(['POST'])
def product_counts_view(request):
    # Load JSON data from the file
    with open('scanned_qr_data.json', 'r') as file:
        products = json.load(file)

    # Extract product names from the loaded data
    product_names = [item.get('PRODUCT NAME') for item in products]

    # Count occurrences of each product name
    product_count = defaultdict(int)
    for name in product_names:
        product_count[name] += 1

    # Convert product_count dictionary to JSON format
    json_output = dict(product_count)

    # Return JSON response
    return JsonResponse(json_output)
