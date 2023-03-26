from django.shortcuts import render , HttpResponse , get_object_or_404
from django.http import  HttpResponseRedirect
from .models import Post
from applications.gymkhana.models import Club_info
# Create your views here.
def addPost(request):
    if request.method == 'POST':
        print("request.POST:", request.POST)
        print("request.FILES:", request.FILES)
        video = request.FILES.get('reel')
        image = request.FILES.get('image')
        text = request.POST.get('desc')
        club_name = request.POST.get('club')

        print(club_name)
        file_type = ""
        club = Club_info.objects.get(club_name=club_name)
        print(club)

        print("video variable:", video)
        print("image variable:", image)
        print("text variable:", text)


        post = Post(
            user=request.user,
            club=club,
            filetype=file_type,
            description=text
        )
        if video:
            post.file.save(video.name, video)
            post.file_type = "video"
        elif image:
            post.file.save(image.name, image)
            post.file_type = "image"

        # debug statements
        print("file saved:", post.file.name)

        # check if the image file was uploaded and saved to the file attribute
        post.save()
    return HttpResponseRedirect('/gymkhana/')

def like(request , post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like(request.user)
    return HttpResponseRedirect('/gymkhana/')


