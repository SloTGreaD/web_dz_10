from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm  # Переконайтеся, що імпортували ваші форми

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Змініть 'index' на ім'я вашого URL для перенаправлення
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user  # Збереження користувача, який додав цитату
            quote.save()
            return redirect('index')  # Аналогічно, змініть на потрібне перенаправлення
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})