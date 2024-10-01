# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# # Create your views here.
#
# def members(request):
#     return render(request, 'Youtube.html')


# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *


# defining function
def youtube(request):
    # checking whether request.method is post or not
    if request.method == 'POST':
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)

        # setting video resolution
        stream = video.streams.get_lowest_resolution()

        # downloads video
        stream.download()

        # returning HTML page
        return render(request, 'Youtube.html')
    return render(request, 'Youtube.html')