from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework_simplejwt.tokens import RefreshToken  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  
from .serializers import LogoutSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            refresh = serializer.validated_data['refresh']
            try:
                RefreshToken(refresh).blacklist()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ObtainTokenView(TokenObtainPairView):  
   def post(self, request, *args, **kwargs):  
      serializer = self.get_serializer(data=request.data)  
      serializer.is_valid(raise_exception=True)  
      refresh = serializer.validated_data['refresh']  
      access = serializer.validated_data['access']  
      return Response({  
        'refresh': str(refresh),  
        'access': str(access),  
      })  
  
class RefreshTokenView(TokenRefreshView):  
   def post(self, request, *args, **kwargs):  
      serializer = self.get_serializer(data=request.data)  
      serializer.is_valid(raise_exception=True)  
      access = serializer.validated_data['access']  
      return Response({  
        'access': str(access),  
      })  
  
class LogoutView(APIView):  
   def post(self, request, *args, **kwargs):  
      try:  
        refresh = request.data['refresh']  
        token = RefreshToken(refresh)  
        token.blacklist()  
        return Response({'message': 'Logged out successfully'})  
      except Exception as e:  
        return Response({'error': str(e)}, status_code=400)
      
