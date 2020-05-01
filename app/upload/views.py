from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def image_upload(request):
    ''' 
    Store the uploaded images
    ''' 
    if request.method == 'POST' and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, 'upload/upload.html', {'image_url':image_url})
    return render(request, 'upload/upload.html')