from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import git


@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            '''
            Auto-update code from GitHub repository
            '''
            repo = git.Repo('/home/josedev/BookStore')  # Caminho correto
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse("✅ Updated code on PythonAnywhere successfully!")
        except Exception as e:
            return HttpResponse(f"❌ Error updating code: {str(e)}")
    else:
        return HttpResponse("""
        <h2>🔄 Auto-Update Endpoint</h2>
        <p>Este endpoint é usado para atualizar automaticamente o código via webhook do GitHub.</p>
        <p><strong>Método:</strong> POST only</p>
        <p><strong>Status:</strong> Disponível</p>
        <hr>
        <a href="/">← Voltar para home</a>
        """)


def hello_world(request):
  template = loader.get_template('hello_world.html')
  return HttpResponse(template.render())