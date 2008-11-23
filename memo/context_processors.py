def memo(request):
    context = {}
    if hasattr(request, 'user') and request.user.is_authenticated():
        context.update({
            'memos': request.user.memo_set.all()
        })
    return context