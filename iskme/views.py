import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Iskme


def index(request):
    if request.method == "POST":
        standard = request.POST.get("standard")
        grade = request.POST.get("grade")
        domain = request.POST.get("domain")
        full_code = request.POST.get("alignment_full_code")
        
        
        result = Iskme.objects.filter(grade=grade,standard=standard,full_code=full_code)
        description = "Nothing Found"
        if result:
            description = result[0].description
            
        iskme_data = Iskme.objects.all()
        data = {
            "alignment_data": iskme_data,
            "description": description
        }
        print(description)
        return render(request, "results.html",data)

    iskme_data = Iskme.objects.all()
    data = {
        "alignment_data": iskme_data
    }
    return render(request, "index.html",data)
def csv(request):
    data = Iskme.objects.all()
    csv_file = request.FILES['file'] # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Uploaded file is not in csv format')    

    file_data = csv_file.read().decode('UTF-8')
   
    lines = file_data.split("\n")
    for i in range(1,len(lines)):                      
        fields = lines[i].split(",")
        try:
            Iskme.objects.create(standard = fields[0], grade = fields[1], \
            end_grade = fields[2], learning_domain = fields[3], full_code = fields[4], \
            description = fields[5])
        except:
            pass

    return render(request, "index.html")