from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EVCharger
from .serializers import EVChargerSerializer
from .utils import haversine

class ChargerSearchAPIView(APIView):
    def get(self, request):
        lat = float(request.GET.get("lat"))
        lon = float(request.GET.get("lon"))
        radius = float(request.GET.get("radius", 500))

        charger_type = request.GET.get("type")
        available = request.GET.get("available")

        qs = EVCharger.objects.filter(is_active=True)

        if charger_type:
            qs = qs.filter(charger_type=charger_type)

        if available == "true":
            qs = qs.filter(is_available=True)

        results = []
        for charger in qs:
            distance = haversine(lat, lon, charger.latitude, charger.longitude)
            if distance <= radius:
                charger.distance = round(distance, 2)
                results.append(charger)

        results.sort(key=lambda x: x.distance)

        serializer = EVChargerSerializer(results, many=True)
        return Response(serializer.data)
