# coding=utf-8
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render_to_response


def get_all_data(request):
    from hospital.models import Ticket

    data = (
        Ticket.objects.filter(date_time__year=2014, date_time__month=8)
                      .values("doctor__speciality__name", "doctor__speciality_id")
                      .annotate(all_tickets=Count("id"), not_empty=Count("patient"))
    )

    return render_to_response(
        "main.html",
        {"data": data}
    )


def get_spec_data(request):
    from hospital.models import Ticket

    spec_id = request.GET["spec_id"]

    data = (
        Ticket.objects.filter(date_time__year=2014, date_time__month=8, doctor__speciality_id=spec_id)
                      .values("doctor__name")
                      .annotate(all_tickets=Count("id"), not_empty=Count("patient"))
    )

    return JsonResponse(list(data), safe=False)