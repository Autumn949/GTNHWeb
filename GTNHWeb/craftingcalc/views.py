from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.template import Context

# Create your views here.

from .models import CraftingQuery
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
def index(request):
    return HttpResponse("index")

from django.shortcuts import redirect

@permission_required("craftingcalc.can_use_craftingcalc", login_url="/craftingcalc/login")
def create_query(request):
    pass

@permission_required("craftingcalc.can_use_craftingcalc", login_url="/craftingcalc/login")
def fetchquery(request):
    current_user = request.user
    print(current_user.id)
    queries = CraftingQuery.objects.filter(uuid= current_user.id)

    print(queries)
    context = {"queries": queries,}
    return render(request, "craftingcalc/fetchquery.html",context)


def login_view(request):

    if(request.method == "POST"):
        print("submitted")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("fetchquery")
        else:
            context = {"login_failed": "True"}
            # Return an 'invalid login' error message.
            return render(request, "craftingcalc/login.html",context )
    else:
        # loads signinpage
        return render(request, 'craftingcalc/login.html')