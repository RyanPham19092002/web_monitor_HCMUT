from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse,HttpRequest
from .models import ToDoList, Item
from .forms import CreateNewList
from django.template import loader
import cv2
# Create your views here.
cap = cv2.VideoCapture(2) 
def choose_camera(response):
    if response.method =="POST":
        #cap.release()
        if response.POST.get("webcam"):
            return HttpResponseRedirect("webcam/") 
        elif response.POST.get("phonecam"):
            return HttpResponseRedirect("phonecam/") 
    return render(response,"web/choose_camera.html")
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id))=="clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            #response.POST = ""
            txt = response.POST.get("new")
            print(len(txt))
            if len(txt) > 2:         
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")    
        elif response.POST.get("delete"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id))=="clicked":
                    item.delete()
        elif response.POST.get("all"):
            for item in ls.item_set.all():
                item.complete = True
                item.save()
        elif response.POST.get("exit"):
            return HttpResponseRedirect('/')
    return render(response,"web/list.html",{"ls" : ls})

def home(response):
    lst = ToDoList.objects
    for lis in lst.all():
            count =0
            for item_list in lis.item_set.all():
                if item_list.complete == False:  
                    count +=1
                    lis.complete_list = False

                if count == 0:
                        lis.complete_list = True
                lis.save()
    for lis in lst.all():
            if response.POST.get("c" + str(lis.id))=="clicked":
                for item_list in lis.item_set.all():
                    item_list.complete = True
                    item_list.save()
    if response.method == "POST":
        if response.POST.get("choose URL"):
            t = int(response.POST.get("choose URL"))
            return HttpResponseRedirect("/%i" %t)
        # elif response.POST.get("new list"):
        #     new_list = response.POST.get("name new list")
        #     t = ToDoList(name=new_list)
        #     t.save()
        elif response.POST.get("delete list"):
            for lis in lst.all():
                if response.POST.get("c" + str(lis.id))=="clicked":
                    ToDoList.objects.get(id=lis.id).delete()
        elif response.POST.get("all list"):
            for lis in lst.all():
                lis.complete_list = True
                lis.save()
        elif response.POST.get("change name list"):
            return HttpResponseRedirect("change/")
    return render(response,"web/home.html",{"lst" : lst})
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)    
    else:
        form = CreateNewList()
    return render(response,"web/create.html",{"form" : form})
def change(response):
    lst = ToDoList.objects
    for lis in lst.all():
            count =0
            for item_list in lis.item_set.all():
                if item_list.complete == False:  
                    count +=1
                    lis.complete_list = False

                if count == 0:
                        lis.complete_list = True
                lis.save()
    for lis in lst.all():
            if response.POST.get("c" + str(lis.id))=="clicked":
                for item_list in lis.item_set.all():
                    item_list.complete = True
                    item_list.save()
    if response.method == "POST":
        if response.POST.get("exit"):
            return HttpResponseRedirect("/") 
    return render(response,"web/change.html")
#//------------------------------------------------------------------
def webcam(request):
    template_webcam = loader.get_template('web/webcam.html') 
    if request.method == "POST":
            if request.POST.get("exit"):
                #cap.release()
                return HttpResponseRedirect("/") 
    return HttpResponse(template_webcam.render({}, request))
def stream_webcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break

        cv2.imwrite('demo.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')
def video_feed_webcam(request): 
    return StreamingHttpResponse(stream_webcam(), content_type='multipart/x-mixed-replace; boundary=frame')

    #/--------------------------------------------------------------

def phonecam(request):
    template_phonecam = loader.get_template('web/phonecam.html') 
    if request.method == "POST":
            if request.POST.get("exit"):
                #cap.release()
                return HttpResponseRedirect("/") 
    return HttpResponse(template_phonecam.render({}, request))
def stream_phonecam():
    cap = cv2.VideoCapture(2)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break

        cv2.imwrite('demo1.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo1.jpg', 'rb').read() + b'\r\n')
def video_feed_phonecam(request): 
    return StreamingHttpResponse(stream_phonecam(), content_type='multipart/x-mixed-replace; boundary=frame')