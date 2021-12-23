from django.shortcuts import render
from .models import UploadFileForm
# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, "demo_file_upload/index.html", {"form": UploadFileForm(), })
    elif request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.POST["title"], request.FILES['file'])
            return render(request, "demo_file_upload/index.html", {"form": UploadFileForm(), "status": "Success!"})
        else:
            return render(request, "demo_file_upload/index.html", {"form": UploadFileForm(), "status": "Fail"})


def upload(file_name, data):
    file = open("file-uploads/" + file_name + "__" + data.name, 'wb+')
    for chunk in data.chunks():
        file.write(chunk)


