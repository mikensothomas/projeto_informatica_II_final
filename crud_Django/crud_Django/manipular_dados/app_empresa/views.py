from django.shortcuts import render
from django.shortcuts import render, redirect  
from app_empresa.forms import GetDadosForm  
from app_empresa.models import App_empresa  
 
def salDados(request):  
    if request.method == "POST":  
        form = GetDadosForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/dados')  
            except:  
                pass  
    else:  
        form = GetDadosForm()  
    return render(request,'index.html',{'form':form})  
def dados(request):  
    getDados = App_empresa.objects.all()  
    return render(request,"dados.html",{'getDados':getDados})  
def editar(request, id):  
    getDados = App_empresa.objects.get(id=id)  
    return render(request,'editar.html', {'getDados':getDados})  
def atualizar(request, id):  
    getDados = App_empresa.objects.get(id=id)  
    form = GetDadosForm(request.POST, instance = getDados)  
    if form.is_valid():  
        form.save()  
        return redirect("/dados")  
    return render(request, 'editar.html', {'getDados': getDados})  
def excluir(request, id):  
    getDados = App_empresa.objects.get(id=id)  
    getDados.delete()  
    return redirect("/dados")