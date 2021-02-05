from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from files.models import InternmentHistory


def internment_list(request):

    activeInternments = InternmentHistory.objects.filter(
        Q(is_interned__exact="True")).distinct().order_by('-entry_date')
    paginator = Paginator(activeInternments, 10)
    page = request.GET.get('page')
    activeInternments = paginator.get_page(page)

    context = {
        'internments': activeInternments,
    }

    return render(request, 'internment/internment_list.html', context)


def delete_internment(request):
    internmentHistory_id = request.POST.get('internmentHistory_id', None)
    print(internmentHistory_id)
    InternmentHistory.objects.filter(id=internmentHistory_id).delete()
    return JsonResponse({})