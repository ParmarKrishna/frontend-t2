from django.shortcuts import render
from .models import ApplyLeave, BranchDetails,Calculation, HeadManager,Login,Employee,BranchManager,PastUserRecords,EmployeeLeaveManagement,GeneralService, Resignation
from django.db import connection
def home(request):
    if request.method=="POST":
        print(request.POST)
        req=request.POST
        mainD={}
        for x,y in req.items():
            if x!="csrfmiddlewaretoken":
                mainD.update({x:y})
        userid=Login.objects.filter(user_id=mainD['userid']).first()
        if userid:
            if userid.password==mainD['password']:
                if userid.role==mainD['role']:
                    print("OK")
                    if mainD['role'].lower() == 'employee':
                        emp=Employee.objects.filter(employee_id=mainD['userid']).first()
                        leaves=ApplyLeave.objects.filter(employee_id=mainD['userid'])
                        context={
                            'info':emp,
                            'title':'Employee',
                            'leaves':leaves
                        }
                        return render(request,'frontendapp/eview.html',context)
                    elif mainD['role'].lower()=='branch_manager':
                        bm=BranchManager.objects.filter(branch_manager_id=mainD['userid']).first()
                        elm=EmployeeLeaveManagement.objects.filter(branch_id=bm.branch_id)
                        #gs=GeneralService.objects.filter(branch_id=bm.branch_id)
                        pus=PastUserRecords.objects.filter(branch_id=bm.branch_id)
                        cals=Calculation.objects.filter(branch_id=bm.branch_id)
                        context={
                            'info':bm,
                            'title':'Branch Manager',
                            'elm':elm,
                            'pus':pus,
                            'cal':cals
                        }
                        return render(request,'frontendapp/bview.html',context)
                    elif mainD['role'].lower()=='head_manager':
                        hm=HeadManager.objects.filter(head_manager_id=mainD['userid']).first()
                        bd=BranchDetails.objects.all()
                        context={
                            'info':hm,
                            'bd':bd
                        }
                        return render(request,'frontendapp/hmview.html',context)

    return render(request,'frontendapp/base.html')

def apply(request):
    print(request.POST)
    if request.method=="POST":
        req=request.POST
        mainD={}
        for x,y in req.items():
            if x!="csrfmiddlewaretoken":
                mainD.update({x:y})
        leave_id=ApplyLeave.objects.last().leave_id+1
        employee_id=Employee.objects.get(employee_id=mainD['empid']).employee_id
        leave_date=mainD['leave_date']
        leave_reason=mainD['leave_reason']
        leave_status='TRUE'
        newl=ApplyLeave(leave_id=leave_id,employee_id=employee_id,leave_reason=leave_reason,leave_date=leave_date,leave_status=leave_status)
        newl.save()
        
    return render(request,'frontendapp/apply.html')

def eview(request):
    is_resign=0
    req=request.POST
    mainD={}
    for x,y in req.items():
        if x!="csrfmiddlewaretoken":
            mainD.update({x:y})
    print(mainD)
    if Resignation.objects.get(mainD['empid']):
        is_resign=1
    context={
        'info':Employee.objects.filter(employee_id=mainD['empid']).first(),
        'title':'Employee',
        'leaves':ApplyLeave.objects.filter(employee_id=mainD['empid']),
        'is_resign':is_resign
    }
    return render(request,'frontendapp/eview.html',context)

def resign(request):
    if request.POST:
        print("In resign")
        req=request.POST
        mainD={}
        for x,y in req.items():
            if x!="csrfmiddlewaretoken":
                mainD.update({x:y})
        Resignation(employee=Employee.objects.get(employee_id=mainD['empid']),resign_reason=mainD['resign_reason'],resign_date=mainD['resign_reason']).save()
    return render(request,'frontendapp/resign.html')