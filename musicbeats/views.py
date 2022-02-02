from django.shortcuts import render
from musicbeats.models import Song, Watchlater
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
# Create your views here.

def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']
        watch = watchlater.objects.filter(user=user)
        for i in watch:
            if video_id == i.video_id:
                message = "Your Video is Already Added"
                break
            else:
                watchlater = Watchlater(user=user, video_id=video_id)
                watchlater.save()
                message = "Your Video is successfully added"
            return redirect(f"/musicbeats/songs/{video_id}", {'message': message})

    return render(request, "musicbeats/watchlater.html")


def index(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/index.html', {'song': song})


def songs(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/songs.html', {'song': song})


def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'musicbeats/songpost.html', {'song': song})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)
        redirect("/")
    return render(request, 'musicbeats/login.html')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=pass1)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    return render(request, 'musicbeats/signup.html')
