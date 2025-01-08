from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BusinessCard
from .forms import BusinessCardForm

def dashboard(request, unique_id):
    card = get_object_or_404(BusinessCard, unique_id = unique_id)
    is_owner = request.user == card.user
    return render(request, 'dashboard.html', {'card': card, 'is_owner': is_owner})

@login_required
def edit_card(request):
    card = get_object_or_404(BusinessCard, user=request.user)
    if request.method == 'POST':
        form = BusinessCardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BusinessCardForm(instance=card)
    return render(request, 'edit_card.html', {'form': form, 'card': card})

