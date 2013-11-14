from django.db import models

# Clase para saber cuando se han hecho modificaciones a nuestro modelo
# y cuando fueron creados los objetos
# Sirve para poder hacer auditorias


class AuditedModel(models.Model):
    # Para que guarde la fecha y hora de cuando se creo el objeto
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(AuditedModel):
    title = models.CharField(max_length=50, unique=True)
    img = models.ImageField(upload_to='media/')
    content = models.CharField(max_length=50000)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.lower().replace(' ', '-')
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
