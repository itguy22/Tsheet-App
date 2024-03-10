from django.shortcuts import render
from .forms import TSheetForm
from .models import TSheet

def create_tsheet(request):
    if request.method == 'POST':
        form = TSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TSheetForm()
    return render(request, 'tsheetapp/create_tsheet.html', {'form': form})

def display_tsheets(request):
    tsheets = TSheet.objects.all()
    return render(request, 'tsheetapp/display_tsheets.html', {'tsheets': tsheets})

