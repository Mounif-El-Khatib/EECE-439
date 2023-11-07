from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import ContactList
# Create your views here.


def checkIfValid(string1, string2):
    valid = True
    n = len(string1)
    counter = 0
    for i in range(n):
        if string1[i] != string2[i]:
            counter += 1
    if counter > 1:
        valid = False
    return valid


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = ContactList(
                User_id=form.cleaned_data["User_id"],
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                profession=form.cleaned_data['profession'],
                profession2=form.cleaned_data['profession2'],
                Phone_Number=form.cleaned_data['Phone_Number'],
                email=form.cleaned_data['email'],
            )
            if (checkIfValid(new_user.profession, new_user.profession2)):
                new_user.save()
                return render(request, 'go_back.html')
            else:
                return render(request, 'error.html')
        else:
            return render(request, "error.html")
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})


def display_contacts(request):
    contacts = ContactList.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def delete(request, user_id):
    contacts = ContactList.objects.all()
    contact = get_object_or_404(ContactList, User_id=user_id)
    contact.delete()
    return render(request, 'contact_list.html', {'contacts': contacts})


def display_homepage(request):
    return render(request, 'home.html')


def update_contact(request, user_id):
    contact = get_object_or_404(ContactList, User_id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = UserForm(instance=contact)

    return render(request, 'update_contact.html', {'form': form, 'contact': contact})
