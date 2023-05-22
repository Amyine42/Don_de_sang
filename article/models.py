from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    age = models.DateField()
    phone_number = models.CharField(max_length=20)
    gender_choices = (
        ("male", 'm'),
        ("female", 'f'),
    )
    gender = models.CharField(max_length = 10,
        choices=gender_choices)
    blood_type_choices = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("autre", "autre"),
    )
    blood_type = models.CharField(max_length = 10,
        choices=blood_type_choices)
    yes_no_choices = (
        ('oui', 'oui'),
        ('non', 'non'),
    )
    blood_donation = models.CharField(max_length = 10,
        choices=yes_no_choices)
    second_question = models.CharField(max_length = 10,
        choices=yes_no_choices)
    third_question = models.CharField(max_length = 10,
        choices=yes_no_choices)
    fourth_question = models.CharField(max_length = 10,
        choices=yes_no_choices)
    fifth_question = models.CharField(max_length = 10,
        choices=yes_no_choices)
    sixth_question = models.CharField(max_length = 10,
        choices=yes_no_choices)
    seventh_question = models.CharField(max_length = 10,
        choices=yes_no_choices)
