from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import MediaForm
from .models import Media

def media_list(request):
    media_files = Media.objects.all()
    return render(request, 'media/list.html', {'media_files': media_files})

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.temp import NamedTemporaryFile

from PIL import Image, ImageOps
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.temp import NamedTemporaryFile

def upload_file(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['file']
            img_temp = NamedTemporaryFile()
            img_temp.write(image.read())
            img_temp.flush()
            img = Image.open(img_temp)
            img = ImageOps.exif_transpose(img)  # automatically orient the image
            img.thumbnail((190, 190))  # resize the image
            img.save(img_temp.name, 'JPEG')
            img_temp.seek(0)
            new_image = SimpleUploadedFile(image.name, img_temp.read(), content_type='image/jpeg')
            form.instance.file = new_image
            form.save()
            img_temp.close()
            return redirect('media_list')
    else:
        form = MediaForm()
    return render(request, 'media/upload.html', {'form': form})


