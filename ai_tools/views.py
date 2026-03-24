from django.shortcuts import render
from .models import Trending,Frontend_AI,Backend_AI,Database_AI,AI_chatbot,Code_generation,UI_UX_Design,Devops_Deployment,Testing_Security
# Create your views here.
def ai_tools(request):
    trending=Trending.objects.all()
    frontend=Frontend_AI.objects.all()
    backend=Backend_AI.objects.all()
    database=Database_AI.objects.all()
    ai_chatbot=AI_chatbot.objects.all()
    code_generation=Code_generation.objects.all()
    ui_ux_design=UI_UX_Design.objects.all()
    devops_deployment=Devops_Deployment.objects.all()
    testing_security=Testing_Security.objects.all()
    data={
        "trending":trending,
        "frontend":frontend,
        "backend":backend,
        "database":database,
        "ai_chatbot":ai_chatbot,
        "code_generation":code_generation,
        "ui_ux_design":ui_ux_design,
        "devops_deployment":devops_deployment,
        "testing_security":testing_security
    }
    return render(request,"ai_tools/ai_page.html",data)