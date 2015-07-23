from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, QueryDict

from tiersheet.models import Player
# Create your views here.
def index(request):

    if request.method == 'POST':
        players = QueryDict(request.POST['content'])

        for index, player_id in enumerate(players.getlist('player[]')):
            player = Player.objects.get(id=player_id)
            player.rank = index
            player.save()

    qb_list  = Player.objects.filter(position="QB")
    rb_list  = Player.objects.filter(position="RB")
    wr_list  = Player.objects.filter(position="WR")
    te_list  = Player.objects.filter(position="TE")
    def_list = Player.objects.filter(position="DEF")
    k_list   = Player.objects.filter(position="PK")

    context = {'qb_list': qb_list, 'rb_list': rb_list, 'wr_list': wr_list, 'te_list': te_list, 'def_list': def_list, 'k_list': k_list}

    return render_to_response('index.html', context, context_instance=RequestContext(request))
