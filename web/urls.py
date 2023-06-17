from django.urls import path
from . import views
urlpatterns = [
path("<int:id>", views.index, name = "index"),
path("homepage/", views.home, name ="home"),
path("create/", views.create, name ="create"),
#path("change/", views.change, name ="change"),
path('choose_camera/', views.choose_camera, name='choose_camera'),

path("choose_camera/webcam/", views.webcam, name ="webcam"),
path("video_feed_webcam/", views.video_feed_webcam, name="video-feed-webcam"),

path("choose_camera/phonecam/", views.phonecam, name ="phonecam"),
path("video_feed_phonecam/", views.video_feed_phonecam, name="video-feed-phonecam"),


] 