from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    blank = text.replace(' ', '')

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_x = sorted(word_dictionary, key=word_dictionary.get, reverse=True)
    sorted_list = [(key, word_dictionary[key]) for key in sorted_x][:5]
    return render(request, 'result.html', {'full': text, 'total': len(text), 'noblank': len(blank), 'dictionary': sorted_list})

