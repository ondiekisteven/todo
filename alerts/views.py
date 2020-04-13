from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlertItemSerializer

from django.shortcuts import render, HttpResponse
from .models import AlertItem

# Create your views here.
def index(request):
    if request.method == 'GET':
        alerts = AlertItem.objects.all().order_by('-pk')
        context = {
            'alerts': alerts
        }
        return render(request, 'alerts/alert.html', context=context)
    if request.method == 'POST':
        message = request.POST['message']
        state = request.POST['state']
        dashboardId = request.POST['dashboardId']

        alert = AlertItem()
        alert.message = message
        alert.state = state
        alert.dashboardId = dashboardId

        alert.save()
        return HttpResponse({'message': 'success'})

class AlertList(APIView):
    
    def get(self, request):
        alerts = AlertItem.objects.all().order_by('-pk')
        serializer = AlertItemSerializer(alerts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AlertItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

        
