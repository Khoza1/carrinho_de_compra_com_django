from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto, CarrinhoItem
import json

@csrf_exempt
def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        produto_id = data.get('produto_id')

        if produto_id:
            produto = Produto.objects.get(id=produto_id)
            usuario = request.user

            if produto:
                print("So dessa funçao entrar aqui significa muitooooo",produto_id)
                # Verifique se o item já existe no carrinho
                item_existente = CarrinhoItem.objects.filter(produto=produto).first()

                if item_existente:
                    item_existente.quantidade += 1
                    item_existente.save()
                else:
                    CarrinhoItem.objects.create(produto=produto)

                return JsonResponse({'message': 'Produto adicionado ao carrinho com sucesso!'})

    return JsonResponse({'message': 'Erro ao adicionar o produto ao carrinho!'}, status=400)

@csrf_exempt
def remover_do_carrinho(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        produto_id = data.get('produto_id')

        if produto_id:
            produto = Produto.objects.get(id=produto_id)
            usuario = request.user

            if produto and usuario:
                item_existente = CarrinhoItem.objects.filter(produto=produto, usuario=usuario).first()

                if item_existente:
                    if item_existente.quantidade > 1:
                        item_existente.quantidade -= 1
                        item_existente.save()
                    else:
                        item_existente.delete()

                    return JsonResponse({'message': 'Produto removido do carrinho com sucesso!'})

    return JsonResponse({'message': 'Erro ao remover o produto do carrinho!'}, status=400)




def index(request):
    produtos=Produto.objects.all()
    return render(request,'appte/index.html',{'produtos': produtos})


#@csrf_exempt
"""
def adicionar_item(request):
    from django.shortcuts import render
    from django.http import JsonResponse
    from .models import Item
    import json
    if request.method == 'POST':
        data = json.loads(request.body)
        nome_item = data.get('nome')

        if nome_item:
            novo_item = Item(nome=nome_item)
            novo_item.save()

            return JsonResponse({'message': 'Item adicionado com sucesso!'})

    return JsonResponse({'message': 'Erro ao adicionar o item!'}, status=400)
    


def index(request):
    return render(request,'appte/index.html')
"""