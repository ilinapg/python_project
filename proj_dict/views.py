from django.shortcuts import render
from django.core.cache import cache
from . import dictionary_work


def index(request):
    return render(request, "index.html")


def dictionary_list(request):
    dictionary = dictionary_work.get_dictionary_for_table()
    return render(request, "dictionary_list.html", context={"dictionary": dictionary})


def add_term(request):
    return render(request, "term_add.html")

def train(request):
    task, ans = dictionary_work.get_task()
    print(task, ans)
    return render(request, "train.html", context={"task": task, "ans": ans})

def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name").replace(";", ",")
        word = request.POST.get("new_term", "").replace(";", ",")
        translation = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(translation) == 0:
            context["success"] = False
            context["comment"] = "Заполните перевод"
        elif len(word) == 0:
            context["success"] = False
            context["comment"] = "Укажите слово"
        else:
            context["success"] = True
            context["comment"] = "Добавлено в словарь"
            dictionary_work.write_word(word, translation)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = dictionary_work.get_dictionary_stats()
    return render(request, "stats.html", stats)

def right(request):
    return render(request, "right.html")

def wrong(request):
    return render(request, "wrong.html")