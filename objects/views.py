# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.http import HttpResponse

from objects.models import Object
from trader.models import Trader
from objects.forms import ObjectForm
import json

def index(request):
	return render(request, 'skeleton.html')



class ObjectCreateView(CreateView):
    model = Object
    form_class = ObjectForm
    template_name = 'objects/object_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return redirect('trader.views.profile')





class ObjectDetailView(DetailView):
    model = Object
    template_name = 'objects/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

    def get(self,request):
    	owner_username = request.GET['owner']
    	name = request.GET['name']
    	owner = Trader.objects.get(username=owner_username)
    	item = Object.objects.get(owner=owner,name=name)
    	response = {
    		'owner' : {
    			'name' : owner.username,
    			'imgURL' : owner.image_url()
    		},
    		'object' : {
    			'summary' : item.summary,
    			'imgURL' : item.image.url,
    			'date' : item.date_createdToString(),
    			'description' : item.description 
    		}
    	}

    	print response

    	return HttpResponse(json.dumps(response))



