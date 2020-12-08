from django.urls import path
from .views import listar_fato, criar_fato, update_fato, deletar_fato, criar_vitima, criar_testemunha, criar_autor, index


urlpatterns = [
    path('', index, name= 'index'),
    path('listarfato', listar_fato, name='listar_fato'),
    path('criarfato', criar_fato, name="criar_fato"),
    path('update/<int:id>/', update_fato, name="update_fato"),
    path('deletar_fato/<int:id>/', deletar_fato, name="deletar_fato"),
    path('adicionarvitima', criar_vitima, name="criar_vitima"),
    path('adicionartestemunha', criar_testemunha, name="criar_testemunha"),
    path('adicionarautor', criar_autor, name="criar_autor")
]