from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DoeData
from .serializers import DoeDataSerializer

class FilterDoeDataView(APIView):
    permission_classes = [IsAuthenticated]  # Only logged-in users can access
    def get(self, request):
        print("Received query params:", request.query_params)  # Debugging
        tool_diameter = request.query_params.get('Tool_Diameter')

        if not tool_diameter:
            return Response({"error": "Tool diameter parameter is required."}, status=400)

        data = DoeData.objects.filter(Tool_Diameter=tool_diameter)

        if not data.exists():
            return Response({"message": "No data found for this tool diameter."}, status=404)

        serializer = DoeDataSerializer(data, many=True)  # This will return all fields
        return Response(serializer.data)
