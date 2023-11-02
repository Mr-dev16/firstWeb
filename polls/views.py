from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import UserForm

# from django.template import loader
from .models import Choice, Question, Users


# Create your views here.
def Index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    ## first example
    # template = loader.get_template("polls/index.html")
    # context = {
    #    "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    ## second example

    return render(request, "polls/index.html")


def questions(request, question_id):
    ## first form create error 404
    # try:
    #    question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404("Question does not exits")
    ## second form create error 404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


#def results(request, question_id):
    ## first form create response of results
    # response="You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    ## second form create response of results
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    ## first form create message of vote
    # return HttpResponse("You're voting on question %s." % question_id)
    ## first system vote the question
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        index = question_id
        index += 1
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("questions", args=[index]))


def Abort(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    cancel=Users.abort(True)
    id_question = Users.question_ID(question)
    
    yield
def OptionOne(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("question")
            # Realiza las acciones que desees con los datos ingresados
            # Por ejemplo, guardar en la base de datos, mostrar en un template, etc.
    else:
        forms = UserForm()
    return render(request, "polls/optionOne.html", {"forms": forms})


def OptionTwo(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data["name"]
            years = forms.cleaned_data["years"]
            data = forms.cleaned_data["data"]
            # Realiza las acciones que desees con los datos ingresados
            # Por ejemplo, guardar en la base de datos, mostrar en un template, etc.
    else:
        forms = UserForm()
    return render(request, "polls/optionTwo.html", {"forms": forms})
