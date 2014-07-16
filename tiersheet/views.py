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
            player.order = index
            player.save()

    qb_list = Player.objects.order_by('order')[:2]
    wr_list = Player.objects.order_by('order')[2:]

    context = {'qb_list': qb_list, 'wr_list': wr_list}

    return render_to_response('index.html', context, context_instance=RequestContext(request))
