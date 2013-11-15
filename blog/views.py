from django.views.generic import TemplateView
from . import models


class IndexView(TemplateView):
    #Definimos el modelos
    model = models.Post
    #Definimos el template
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        #Pasamos las variables requeridas dentro del contexto
        # que seran rendereadas en el template
        context = super(IndexView, self).get_context_data(*kwargs)
        # la variable posts es un iterable
        # que trae todos los objetos que contiene el modelo
        context['posts'] = self.model.objects.all()
        return context


class PostView(TemplateView):
    model = models.Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = self.model.objects.filter(slug=context['slug'])
        return context
