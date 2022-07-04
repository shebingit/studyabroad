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




#sherry george

def login(request):
    return render(request,'DocumentOfficer_index.html')
def studens(request):
    return render(request,'councilordashboard.html')#studentscouncilor tab
def sales(request):
    return render(request,'salesnewly.html')  
def newlyleades(request):
    return render(request,'newlyleads.html')    
def currentleadss(request):
    return render(request,'currentleads.html') 
def previousleadss(request):
    return render(request,'previouslyassleads.html')      
def previousdash(request):
    return render(request,'previousleads.html')     
def statuscurrent(request):
    return render(request,'status1.html')      

#dilshad
def dashboard(request):
    return render(request,'dashboard_head.html')    
def team_leader_clints(request):
    return render(request,'clints.html')  
def status_progress(request):
    return render(request, 'status.html')      

# counsilor dashboard
#sambhu
def home(request):
     return render(request,'councilor/home.html')
def currentleads(request):
     return render(request, 'councilor/current_leads.html')
def previousleads(request):
    return render(request, 'councilor/previous_leads.html')
def councilornewlyprofile(request):
    return render(request, 'councilor/councilornewprof.html') 
def status2(request):
    return render(request, 'councilor/counstatus1.html')  
# #eldho    


def signupp(request):
    return render(request,'signup.html')
def newlyassignleads(request):
     return render(request, 'councilor/newly_leads.html')
def status1(request):
    return render(request, 'councilor/counstatus.html')       



def DocumentOfficer_index(request):
    return render(request,"DocumentOfficer_index.html")

def DocumentOfficer_newly_assigned_leads(request):
    return render(request, "DocumentOfficer_newly_assigned_leads.html")

def DocumentOfficer_Previous_leads(request):
    return render(request, "DocumentOfficer_Previous_leads.html")

def DocumentOfficer_index(request):
    return render(request,"DocumentOfficer_index.html")
    
def DocumentOfficer_dashboard(request):
    return render(request,"DocumentOfficer_dashboard.html")
    
def DocumentOfficer_CurrentLeads_table(request):
    return render(request,"DocumentOfficer_CurrentLeads_table.html")
    
def DocumentOfficer_CanadaDocuments(request):
    return render(request,"DocumentOfficer_CanadaDocuments.html")

def DocumentOfficer_UKDocuments(request):
    return render(request,"DocumentOfficer_UKDocuments.html")

def DocumentOfficer_Accsetting(request):
    return render(request,"DocumentOfficer_Accsetting.html")

def DocumentOfficer_Previous_CanadaDocuments(request):
    return render(request,"DocumentOfficer_Previous_CanadaDocuments.html")

def DocumentOfficer_Previous_UKDocuments(request):
    return render(request,"DocumentOfficer_Previous_UKDocuments.html")    

