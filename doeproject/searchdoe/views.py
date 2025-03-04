from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DoeData
from .serializers import DoeDataSerializer


class FilterDoeDataView(APIView):
    permission_classes = [IsAuthenticated]  # Only logged-in users can access

    def post(self, request):  # Change to POST method
        print("Received form data:", request.data)  # Debugging
        tool_diameter = request.data.get('Tool_Diameter')  # Get data from form instead of query
        print(tool_diameter)
        if not tool_diameter:
            return Response({"error": "Tool diameter parameter is required."}, status=400)

        data = DoeData.objects.filter(Tool_Diameter=tool_diameter)

        if not data.exists():
            return Response({"message": "No data found for this tool diameter."}, status=404)

        serializer = DoeDataSerializer(data, many=True)  # Serialize data
        return Response(serializer.data)