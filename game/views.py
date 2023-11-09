from django.shortcuts import render
from django.db import connection
import random
from random import sample
from .models import Game
from record.models import Trash
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GameSettingData(APIView):
    def post(self, request):
        player_name = request.data.get('player_name')
        if not player_name:
            return Response({"error": "player_name is required"}, status=status.HTTP_400_BAD_REQUEST)

        game = Game.objects.create(player_name=player_name)
        if game:
            trash_1 = Trash.objects.filter(difficulty=1)
            trash_2 = Trash.objects.filter(difficulty=2)
            
            random_trash_1 = sample(list(trash_1), 7)
            random_trash_2 = sample(list(trash_2), 3)

            trash_ids = [trash.id for trash in random_trash_1 + random_trash_2]

            random_list = self.generate_random_list()

            response_data = {
                "game_id": game.id,
                "random_list": {str(trash_id): num for trash_id, num in zip(trash_ids, random_list.values())}
            }
        
            print(game.id)
            print(random_list)
            print(trash_ids)

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to create a game"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def generate_random_list(self):
        unique_numbers = random.sample(range(1, 51), 10)
        random_list = {str(i): num for i, num in enumerate(unique_numbers, start=1)}
        return random_list
