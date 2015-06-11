from django.db import models


class Specializzando(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    CF = models.CharField(max_length=16)
    sesso = models.CharField(max_length=1)
    anno_iscrizione = models.PositiveSmallIntegerField(default=0)
    neo = models.BooleanField(default=False)
    mat = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome+' '+self.cognome

    class Meta:
        verbose_name_plural = 'Specializzandi'

class Desiderata(models.Model):
    spec = models.ForeignKey(Specializzando)
    data = models.DateTimeField()
    tipoDesiderata = models.CharField(max_length=1)

    def __unicode__(self):
        return self.spec.nome + ' ' + self.spec.cognome + ' ' + str(self.data)

    class Meta:
        verbose_name_plural = 'Desiderata'

