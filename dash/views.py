import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def form_data(request):
    if request.method == 'POST':
        form_data = request.data.get('data')  # Assuming 'data' is the key for form data
        if form_data:
            # Define the path where you want to save the JSON file
            file_path = 'form_data.json'
            # Read existing data from the JSON file, if it exists
            existing_data = []
            try:
                with open(file_path, 'r') as json_file:
                    existing_data = json.load(json_file)
            except FileNotFoundError:
                pass
            # Append the new form data to the existing data
            existing_data.append(form_data)
            # Write the combined data back to the JSON file
            with open(file_path, 'w') as json_file:
                json.dump(existing_data, json_file)
            return Response({'message': 'Form data saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Form data is required'}, status=status.HTTP_400_BAD_REQUEST)
