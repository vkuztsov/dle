from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntityModelForm;
from .models import EntityModel;
from django.utils import timezone
from django.urls import reverse

import math

def index(request):
    return redirect('/entities/1')

def get_entities_page(request, page_id, entity_list, search_query=None):
    records_per_page = 10
    lower_limit = (page_id - 1) * records_per_page
    upper_limit = lower_limit + records_per_page

    records_count = len(entity_list)

    total_pages = math.ceil( records_count / 10 )
    page_range = range(max(1, page_id - 3), min(total_pages + 1, page_id + 4))

    return render(request, 'entities.html', {'page_id': page_id, 
                                             'page_range': page_range, 
                                             'entities': entity_list[lower_limit:upper_limit], 
                                             'search_query': search_query})

def entities(request, page_id):
    return get_entities_page(request, page_id, EntityModel.objects.all())

def entities_search(request, search_query, page_id = 1):
    return get_entities_page(request, page_id, EntityModel.objects.all().filter(legal_name__icontains=search_query), search_query)

def get_entity(request, entity_id):
    entity = get_object_or_404(EntityModel, id=entity_id)
    return render(request, 'entity.html', {'entity': entity})


def add_entity(request):
    if request.method == 'POST':
        form = EntityModelForm(request.POST)
        if form.is_valid():
            entity = form.save(commit=False)
            entity.date_added = timezone.now()
            entity.save()
            if not 'save_continue_btn' in request.POST:
                return redirect(f'/entity/{entity.id}')
            else:
                return render(request, 'editform.html', {'entity_edit': False, 'info_msg': 'Успішно додано.'})
        else:
            return render(request, 'editform.html', {'entity_edit': False, 'err_msg': list(form.errors.values())[0][0], 'form': form.cleaned_data})
    return render(request, 'editform.html', {'entity_edit': False})


def edit_entity(request, entity_id):
    obj = get_object_or_404(EntityModel, id=entity_id)

    if request.method == 'POST':
        form = EntityModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/entity/{entity_id}')
        else:
            return render(request, 'editform.html', {'entity_edit': True, 'err_msg': list(form.errors.values())[0][0], 'form': form.cleaned_data})
    
    return render(request, 'editform.html', {'entity_edit': True, 'form': obj})


def delete_entity(request, entity_id):
    obj = get_object_or_404(EntityModel, id=entity_id)
    obj.delete()

    return index(request)