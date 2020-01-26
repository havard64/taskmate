from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from diary.models import Diary
from diary.forms import DiaryForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@ login_required
def diary(request):
    if request.method == "POST":
        form = DiaryForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, "Goal/Motto Added!")
        return redirect('diary')
    else:
#        all_diary = Diary.objects.filter(manage=request.user)
#        paginator = Paginator(all_diary, 1)
#        page = request.GET.get('pg')
#        all_tasks = paginator.get_page(page)

        return render(request, 'diary.html') # {'all_diary': all_diary}

