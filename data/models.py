from django.db import models
from django.core.urlresolvers import reverse

class Match(models.Model):
    matchID = models.CharField(max_length=50,primary_key=True)
    win = models.CharField(max_length=250)
    time = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('data:detail', kwargs={'pk' : self.pk})

    def __str__ (self):
        return self.matchID + '-' + self.win  

class Hero(models.Model):
    gameID = models.ForeignKey(Match,on_delete=models.CASCADE)
    HeroName =  models.CharField(max_length=250)
    
    def __str__(self):
        return  self.HeroName