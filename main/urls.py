from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entities/', views.index, name='entities_index'),
    path('entities/<int:page_id>', views.entities, name='entities'),
    path('entities/search/<str:search_query>/<int:page_id>', views.entities_search, name='entities_search_with_page'),
    path('entities/search/<str:search_query>/', views.entities_search, name='entities_search'),
    path('entity/<int:entity_id>', views.get_entity, name='entity'),
    path('entity/add/', views.add_entity, name='add_entity'),
    path('entity/edit/<int:entity_id>', views.edit_entity, name='edit_entity'),
    path('entity/delete/<int:entity_id>', views.delete_entity, name='delete_entity')
]