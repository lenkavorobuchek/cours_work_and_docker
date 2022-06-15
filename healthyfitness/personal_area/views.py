from django.shortcuts import render, redirect
from calculator.models import Profile
from .forms import ImageForm


def PersonalArea(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all().filter(user=request.user)
        return render(request, 'personal_area/personal_area.html', {'profile': profile})
    else:
        return redirect('login')


def image_upload_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid() and request.FILES:
                request.user.profile.photo = request.FILES['photo']
                request.user.save()
                return redirect('personalArea')
        else:
            form = ImageForm()
        return render(request, 'personal_area/change_information.html', {'form': form})
    else:
        return redirect('login')
