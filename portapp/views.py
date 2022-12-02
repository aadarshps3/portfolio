from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')



# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
# Import render module
from django.shortcuts import render

# Define function to download pdf file using template
def download_file(request, filename='ADARSH RESUME.pdf'):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = r"C:\Users\ADARSH PS\PycharmProjects\portfolio\ADARSH RESUME.pdf"
        print(filepath)
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'index.html')