from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserProfileSerializer,ProfileSerializer
from django.urls import reverse_lazy
from django.shortcuts       import render, redirect
from django.contrib.auth    import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

"""
All the work is done in the serializers.py
"""
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    
#only if you want to change the response
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True) 
    #     self.perform_create(serializer)  
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
class ProfileListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
    
class BlackListRefreshToken(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        token = RefreshToken.for_user(request.user)
        token.blacklist()
        return Response("Token blacklisted", status=status.HTTP_205_RESET_CONTENT)
    

class UserDetails(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        # Return the currently logged-in user
        return self.request.user
    


def login_view(request):
    # if they’re already logged in, send them home
    if request.user.is_authenticated:
        return redirect('/')  

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            # honor “next=” or fall back to /
            return redirect(request.GET.get('next', '/'))
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

