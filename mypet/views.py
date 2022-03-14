import json
from django.views import View
from .models import Owners,Dogs
from django.http import JsonResponse
# Create your views here.
class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owners.objects.create (
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({'messasge':'created'}, status=201)
    def get(self, request):
        owners = Owners.objects.all()
        result=[]
        for owner in owners:
            res = []
            dogs= owner.dogs_set.all()
            for dog in dogs:
                res.append(
                    {
                        'name': dog.name,
                        'age' : dog.age
                    }
                )
                result.append(
                    {
                        'name': owner.name,
                        'age': owner.age,
                        'email' : owner.email,
                        'pet_list' : res
                    }
                )
  
        return JsonResponse({'results':result}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owners.objects.get(name=data['owner'])
        Dogs.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id= owner.id,
        )
        return JsonResponse({'message':'created'},status=201)

    def get(self, request):
        dog_list = Dogs.objects.all()
        results=[]
        for dog in dog_list:
            results.append(
                 {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner_name' : dog.owner.name
                }
            )
        return JsonResponse({'results':results},status=200)
