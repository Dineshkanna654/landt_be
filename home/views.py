from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import json
import os

# Define the path to the JSON file
JSON_FILE_PATH = "scanned_qr_data.json"

# Create the JSON file if it doesn't exist
if not os.path.exists(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, "w") as f:
        json.dump([], f)

def is_duplicate(data, existing_data):
    # Check if the data is already present in the existing_data
    for item in existing_data:
        if item == data:
            return True
    return False

@csrf_exempt
def scan_qr_code(request):
    if request.method == 'POST':
        # Extract PNG image data from request
        image_data = request.FILES.get('image_data')

        if not image_data:
            return JsonResponse({'error': 'No image data found in the request'})

        try:
            # Read image data from request
            with Image.open(image_data) as image:
                # Decode QR code using pyzbar
                decoded_objects = decode(image)

                if decoded_objects:
                    qr_data = decoded_objects[0].data.decode('utf-8')
                    # Process the QR code data as needed
                    # For example, save to database or return directly
                    json_data = json.loads(qr_data)

                    # Load existing data from the file
                    with open(JSON_FILE_PATH, "r") as f:
                        existing_data = json.load(f)
                    
                    # Check if the data is a duplicate
                    if not is_duplicate(json_data, existing_data):
                        # Append the JSON data to the file
                        with open(JSON_FILE_PATH, "w") as f:
                            existing_data.append(json_data)
                            json.dump(existing_data, f, indent=4)

                    return JsonResponse({'qr_data': json_data})
                else:
                    return JsonResponse({'error': 'QR code not found or could not be decoded'})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while processing the image: {}'.format(str(e))})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
from django.http import JsonResponse
import json
import os

# Define the path to the JSON file
JSON_FILE_PATH = "scanned_qr_data.json"

@csrf_exempt
def get_all_data(request):
    if request.method == 'POST':
        try:
            # Check if the JSON file exists
            if os.path.exists(JSON_FILE_PATH):
                # Load data from the file
                with open(JSON_FILE_PATH, "r") as f:
                    all_data = json.load(f)
                return JsonResponse({'all_data': all_data})
            else:
                return JsonResponse({'error': 'No data available'})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while reading the data from the file: {}'.format(str(e))})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
