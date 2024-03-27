from django.shortcuts import render, redirect
from .forms import TSheetForm
from .models import TSheet
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def create_tsheet(request):
    if request.method == 'POST':
        form = TSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_tsheets')
    else:
        form = TSheetForm()
    return render(request, 'tsheetapp/create_tsheet.html', {'form': form})

def display_tsheets(request):
    tsheets = TSheet.objects.all()
    return render(request, 'tsheetapp/display_tsheets.html', {'tsheets': tsheets})

def delete_tsheet(request, tsheet_id):
    if request.method == "POST":
        tsheet = get_object_or_404(TSheet, id=tsheet_id)
        tsheet.delete()
        return redirect('display_tsheets')
    else:
        return HttpResponse("Method not allowed", status=405)