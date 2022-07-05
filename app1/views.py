from django.shortcuts import render


#Shebin Shaji ==> admin

def load_admin(request):
    return render(request,'admin.html')

def load_leads(request):
    return render(request,'admin_leads.html')

def load_concilors(request):
    return render(request,'admin_concilors.html')

def load_docofficers(request):
    return render(request,'admin_docofficers.html')

def load_documets(request):
    return render(request,'admin_document.html')

def load_admin_profile(request):
    return render(request,'admin_profile.html')

def load_cuttentdoc(request):
    return render(request,'admin_currentdoc.html')

def load_completed(request):
    return render(request,'admin_completed.html')

def load_previous_lead(request):
    return render(request,'admin_previs_leads.html')

def load_previous_consilers(request):
    return render(request,'admin_prev_consilers.html')

def load_admin_clients_more(request):
    return render(request,'admin_client_more.html')

def load_admin_client_compstatus(request):
    return render(request,'admin_client_status_comp.html')




