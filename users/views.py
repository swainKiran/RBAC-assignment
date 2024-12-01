from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User, Role
from .serializers import UserSerializer

# Register View
class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, status=400)
        user = User.objects.create_user(email=email, password=password)
        return Response({"message": "User registered successfully"})

# Login View
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Email: {email}, Password: {password}")  # Debug: Check input

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        print(f"Authenticated User: {user}")  # Debug: Check authentication result

        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)

# Protected View (RBAC Example)
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_roles = request.user.roles.all()
        permissions = [role.permissions for role in user_roles]
        return Response({"permissions": permissions})
