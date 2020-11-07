from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'contact_email': request.POST['contact_email'],
            'contact_phone': request.POST['contact_phone'],
            'subject': request.POST['subject'],
            'message': request.POST['message'],
        }
        
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

            #return redirect(reverse('contact_success')

        else:
            messages.error(request, "Sorry there was a problem, please check the information you have provided")
    
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact_page.html', context)