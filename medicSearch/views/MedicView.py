from django.shortcuts import render
from medicSearch.models import Profile
from django.db.models import Q

def list_medic_view(request):
    name = request.GET.get('name') 
    speciality = request.GET.get('speciality') 
    neighborhood = request.GET.get('neighborhood') 
    city = request.GET.get('city') 
    state = request.GET.get('state') 

    medics = Profile.objects.filter(role=2)
    if name is not None and name != '': 
        # user__first_name__contains => Está procurando dentro da Foreing Key User de Profile a tabela
        # first name sem fazer a distinção, entre letras maiúsculas e minúsculas
        medics = medics.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name)) 
    
    if speciality is not None: 
        medics = medics.filter(specialties__id=speciality)
    
    if neighborhood is not None: 
        medics = medics.filter(addresses__neighborhood__id=neighborhood)

    else:
        if city is not None: 
            medics = medics.filter(addresses__neighborhood__city__id=city) 

        elif state is not None: 
            medics = medics.filter(addresses__neighborhood__city__state__id=state) 
  
    context = {
        'medics':medics
    }

    return render(request, template_name='medic/medics.html', context=context, status=200)

