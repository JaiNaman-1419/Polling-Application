from django.http import HttpResponseRedirect


def redirect_to_polls(request):
    return HttpResponseRedirect('/polls')
