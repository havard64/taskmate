from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from diary.models import Diary
from diary.forms import DiaryForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime


@ login_required
def diary(request):
    if request.method == "POST":
        form = DiaryForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, "MyDay Added!")
        return redirect('log')
#    else:
#        if Diary.objects.filter(date=datetime.date.today()).exists():
#            template = 'diary.html'
#            day = Diary.objects.get(date=datetime.date.today())
#            daypk = day.pk
#            form = DiaryForm(instance=day)
#           context = {
#                'form': form,
#                'day': day,
#            }
#            return render(request, template, context)
#            return render(request, 'diary_edit.html')
#            return redirect('diary_edit', daypk)
#            return render(request, 'diary.html')
    else:
        return render(request, 'diary.html')

@login_required
def diary_edit(request, pk):
    template = 'diary_edit.html'
    day = get_object_or_404(Diary, pk=pk)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=day)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Your MyDay is updated")

        except Exception as e:
            messages.warning(request, 'Your update was not saved due to an error: {}'.format(e))

    else:
        form = DiaryForm(instance=day)

    context = {
      'form': form,
       'day': day,
    }

    return render(request, template, context)


@login_required
def log(request):
    all_diary = Diary.objects.filter(manage=request.user).order_by('-date')
    return render(request, 'log.html', {'all_diary': all_diary})


@login_required
def diary_delete(request, pk):
    diary = Diary.objects.get(pk=pk)
    if diary.manage == request.user:
        diary.delete()
    else:
        messages.error(request, "Access restricted, you are not allowed")
    return redirect('log')
