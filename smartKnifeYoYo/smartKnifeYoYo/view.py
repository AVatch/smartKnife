from django.shortcuts						import render_to_response
from django.http							import HttpResponseRedirect
from django.contrib.auth.models				import User
from django.contrib.auth					import authenticate, login
from django.template.loader					import get_template
from django.template						import Context
from django.template						import RequestContext


def homepage_view(request):
	sitename = 'smartKnife'
	context = {'sitename':sitename} #render with vars
	return render_to_response('base.html', context, context_instance=RequestContext(request))


