from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ka.models import Vprasanje, Anketa

# Create your views here.
def user_login(request):
    #preveri, ce gre za http POST, poskusi dobiti usr in pwd
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    #vrne User object:
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Račun neaktiven.")
        else:
            print("Napačni podatki {0}, {1}".format(username, password))
            return HttpResponse("Napačni prijavni podatki.")
    else:
        return render(request, 'ka/login.html', {})

@login_required
def index(request):
    return render(request, 'ka/index.html')

@login_required
def vprasanje(request, ):
    if request.method == 'POST':
        pass

    #ce je zacel na strani, ustvari novo anketo, prikazi prvo vprasanje
    else:
        anketa = Anketa.objects.create()
        vprasanja = anketa.seznam_vprasanj()
        #odgovori = anketa.seznam_odgovorov()
        paginator = Paginator(vprasanja, 1)

        page = request.GET.get('page')
        try:
            vprasanje = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            vprasanje = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            vprasanje = paginator.page(paginator.num_pages)





        context_dict = {'vprasanje': vprasanje} #'odgovori': odgovori}
        return render(request, 'ka/vprasanje.html', context_dict)
