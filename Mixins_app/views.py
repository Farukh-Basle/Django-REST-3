from django.shortcuts import render
from Mixins_app.models import Emp
from Mixins_app.serializers import EmpSerializer
from rest_framework import mixins,generics

# Create your views here.
class EmpListView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Emp.objects.all()    #orm_query
    serializer_class = EmpSerializer    #conv into dict

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)



class EmpDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Emp.objects.all()    #orm_query
    serializer_class = EmpSerializer    #conv into dict

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)


    def delete(self,request,pk):
        return self.destroy(request)