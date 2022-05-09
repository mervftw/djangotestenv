from django.shortcuts import render
from teston.models import User
from teston.forms import NewUserForm
from teston.forms import FormName
# Create your views here.


def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'teston/users.html',{'form':form})


def index(request):
    return render(request,'teston/index.html')

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING HERE
            print("VALIDATION SUCCESS!")
            print("NAME: "+ form.cleaned_data['name'])
            print("email: "+ form.cleaned_data['email'])
            print("TEXT: "+ form.cleaned_data['text'])


    return render(request,'teston/form_page.html',{'form': form})