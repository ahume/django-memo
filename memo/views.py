from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from memo.models import Memo

def user_inbox(request, template='memo/list.html'):
    context = {
        'memos': Memo.objects.filter(user=request.user)
    }
    return render_to_response(template, context,
                              context_instance=RequestContext(request))
    
def memo_delete(request, pk):
    Memo.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/messages/')