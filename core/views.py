from django.shortcuts import render, HttpResponse


# Create your views here.

html_base = """
    <h1>Hello world</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
    </ul>
"""

def home(request):
    html_response = "<h1>Mi Web Personal</h1>"
    for i in range(10):
        html_response += "<p>Esto es la portada</p>"
    return HttpResponse(html_base + html_response)

def about(request):
    return HttpResponse(html_base + """
        <h1>Mi Web Personal</h1>
        <h2>Acerca de</h2>
        <p>Now I've become death, destroyer of the worlds</p>
    """)

def home(request):
    return render(request, "core/home.html")