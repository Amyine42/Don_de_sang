from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Survey

def articleAccueil(request):
    return render(request,"index.html")

def desc(request):
    return render(request,"article/pk.html")

def qui(request):
    return render(request,"article/qui.html")

def oudonner(request):
    return render(request,'article/oudonner.html')

def contact(request):
    return render(request,'article/contact.html')

def thankyou(request):
    return render(request, 'article/thankyou.html')

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            fname = form.cleaned_data['fname']
            age = form.cleaned_data['age']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            blood_type = form.cleaned_data['blood_type']
            blood_donation = form.cleaned_data['blood_donation']
            second_question = form.cleaned_data['second_question']
            third_question = form.cleaned_data['third_question']
            fourth_question = form.cleaned_data['fourth_question']
            fifth_question = form.cleaned_data['fifth_question']
            sixth_question = form.cleaned_data['sixth_question']
            seventh_question = form.cleaned_data['seventh_question']

            # Save form data
            Survey.objects.create(
                name = name,
                fname = fname,
                age = age,
                phone_number = phone_number,
                gender = gender,
                blood_type = blood_type,
                blood_donation = blood_donation,
                second_question = second_question,
                third_question = third_question,
                fourth_question = fourth_question,
                fifth_question = fifth_question,
                sixth_question = sixth_question,
                seventh_question = seventh_question
                )
            return redirect('thankyou')
    else:
        form = SurveyForm()

    return render(request, 'article/survey.html', {'form': form})
