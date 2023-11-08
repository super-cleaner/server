from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models.record import Record
from .models.trash import Trash, TrashCategory
from game.models.game import Game

# Create your views here.


def main(request):
    if request.method == 'POST':
        game_id=request.POST.get('game_id')
        trash_id=request.POST.get('trash_id')

        trash=get_object_or_404(Trash, id=trash_id)
        game= get_object_or_404(Game, id_game_id)

        record=Record.objects.create(game=game, trash=trash)

        quiz_data = {
            'trash':{
                'trash_name': trash.name,
                'image_url':trash.image_url,
            }
        }

        return JsonResponse(quiz_data)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


def check(request):
    if request.method == 'POST':
        game_id=request.POST.get('game_id')
        trash_id=request.POST.get('trash_id')
        player_trash_category_id=request.POST.get('player_trash_category_id')

        game=get_object_or_404(Game,id=game_id)
        trash=get_object_or_404(Trash, id=trash_id)
        is_answer=(trash.trash_category.id==player_trash_category_id)

        # 정답 여부에 따라서 record에 기입
        record=get_object_or_404(Record, game=game, trash=trash)
        record.is_answer=is_answer
        record.save()

        quiz_check_data={
            'trash':{
                'trash_name': trash.name,
                'trash_category_name':trash.trash_category.name,
                'is_answer':is_answer,
            }
        }

        return JsonResponse(quiz_check_data)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def result(request, game_id):
    if request.method =='GET':
        game=get_object_or_404(Game, id=game_id)
        records = Record.objects.filter(game=game)
        result_list = {}

        score=0  #socre 계산
        for index, record in enumerate(records):
            if record.is_answer: #record의 is_answer가 true인 경우만 score+=1
                score+=1

            result_list[f'trash{index+1}']={
                'trash_name': record.trash.name,
                'trash_category_name': record.trash.trash_category.name,
                'is_answer': record.is_answer,
            }

        if score<=3:  #점수에 따른 description(멘트)
            description='아직 지구를 구하기에는 부족해…'
        else:
            description='같이 지구를 구해줘서 고마워!'

        quiz_result_data = {
            'score': score,
            'description': description,
            'result_list':result_list,
        }

        return JsonResponse(quiz_result_data)


    return JsonResponse({'error': 'Invalid request'}, status=400)