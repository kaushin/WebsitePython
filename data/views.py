from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Match

class IndexView(generic.ListView):
    template_name = 'data/index.html'
    context_object_name = 'matches'
   
    def get_queryset(self):
        return Match.objects.all()

class DetailView(generic.DetailView):
    model = Match
    context_object_name = 'match'
    template_name = 'data/detail.html'

class MatchCreate(CreateView):
    model = Match
    fields = ['matchID','win','time']

class MatchUpdate(UpdateView):
    model = Match
    fields = ['matchID','win','time']

class MatchDelete(DeleteView):
    model = Match
    success_url = reverse_lazy('data:index')
    

# def index(request):
#     matches = Match.objects.all()
#     context = {
#         'matches' : matches,
#     }
#     return render(request, "data/index.html" , context)

# def detail(request, matchid):
#     match =get_object_or_404(Match, matchID=matchid)
#     return render(request, "data/detail.html" , {'match' : match})

def flip_win(request):
    try:
    
        match =get_object_or_404(Match ,matchID=request.POST['match'])
    
    except (KeyError, Match.DoesNotExist):
    
        matches = Match.objects.all()
        context = {
            'matches' : matches,
            'error_message' : 'You did not select a valid Match '
        }
        return render(request, "data/index.html" , context)
    
    else:

        if(match.win == 'Dire'):
            match.win = 'Radiant'
        else:
            match.win = 'Dire'

        match.save()
        matches = Match.objects.all()
        context = {
            'matches' : matches,
        }
        return render(request, "data/index.html" , context)