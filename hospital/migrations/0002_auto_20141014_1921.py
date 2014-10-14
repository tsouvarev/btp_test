# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def init_data(apps, schema_editor):

    Speciality = apps.get_model("hospital", "Speciality")
    Doctor = apps.get_model("hospital", "Doctor")
    Patient = apps.get_model("hospital", "Patient")
    Ticket = apps.get_model("hospital", "Ticket")

    create_speciality = lambda name: Speciality.objects.create(name=name)

    specialities = [
        None,
        create_speciality(u"Терапевт"),
        create_speciality(name=u"Травматолог"),
        create_speciality(name=u"Педиатр"),
        create_speciality(name=u"Психиатр"),
    ]

    create_doctor = lambda name, speciality_id: Doctor.objects.create(name=name, speciality=specialities[speciality_id])

    doctors = [
        None,
        create_doctor(u"Быков Андрей Евгеньевич", 1),
        create_doctor(u"Лобанов Семён Семёнович", 2),
        create_doctor(u"Левин Борис Аркадьевич", 1),
        create_doctor(u"Черноус Варвара Николаевна", 3),
        create_doctor(u"Ульянова Полина Сергеевна", 3),
        create_doctor(u"Калинина Софья Яковлевна", 3),
        create_doctor(u"Корнеев Максим Леонидович", 4),
    ]

    create_patient = lambda name: Patient.objects.create(name=name)

    patients = [
        None,
        create_patient(u"Романенко Глеб Викторович"),
        create_patient(u"Мальцев Алексей Денисович"),
        create_patient(u"Скрябина Любовь Михайловна"),
        create_patient(u"Королёва Маргарита Павловна"),
        create_patient(u"Ярославский Антон Павлович"),
    ]

    from datetime import datetime
    create_ticket = lambda doctor_id, date_time, patient_id: Ticket.objects.create(
        doctor=doctors[doctor_id], date_time=datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S"),
        patient=patients[patient_id] if patient_id else None
    )

    tickets = [
        create_ticket(1, "2014-08-10 12:00:00", None),
        create_ticket(1, "2014-08-10 12:15:00", None),
        create_ticket(1, "2014-08-10 12:30:00", 5),
        create_ticket(1, "2014-08-11 12:00:00", None),

        create_ticket(2, "2014-08-10 12:00:00", 1),
        create_ticket(2, "2014-08-10 12:15:00", None),
        create_ticket(2, "2014-08-10 12:30:00", None),
        create_ticket(2, "2014-08-11 12:00:00", 5),

        create_ticket(4, "2014-08-10 12:00:00", 1),
        create_ticket(4, "2014-08-10 12:15:00", 3),
        create_ticket(4, "2014-08-10 12:30:00", None),
        create_ticket(4, "2014-08-11 12:00:00", 1),

        create_ticket(7, "2014-08-10 12:00:00", 4),
        create_ticket(7, "2014-08-10 12:15:00", 3),
        create_ticket(7, "2014-08-10 12:30:00", 2),
        create_ticket(7, "2014-08-11 12:00:00", 1),

        create_ticket(5, "2014-08-10 12:00:00", 4),
        create_ticket(5, "2014-08-10 12:15:00", 3),
        create_ticket(5, "2014-08-10 12:30:00", 2),
        create_ticket(5, "2014-08-11 12:00:00", 1),
    ]


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_data)
    ]
