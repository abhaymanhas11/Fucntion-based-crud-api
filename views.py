from django.shortcuts import render
from .models import student
from .serializers import stu_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def studentdata(request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=student.objects.get(id=id)
            s=stu_serializer(stu)
            return Response(s.data)
        stu = student.objects.all()
        s = stu_serializer(stu,many=True)
        return Response(s.data)


    if request.method=='POST':
        serializer=stu_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'})
        return Response(serializer.errors)

    if request.method=='PUT':
        id=request.data.get('id')
        stu=student.objects.get(id=id)
        serializer=stu_serializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated '})
        return Response(serializer.errors)

    if request.method =='DELETE':
        id=request.data.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Deleted successfully'})