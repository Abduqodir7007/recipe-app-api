from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from recipe import serializers
from core.models import Recipe


class RecipeView(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all() 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)