from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseList(APIView):
    def get(self, request, category=None):
        user = request.user.id
        if category is not None:
            expenses = Expense.objects.filter(user=user, category=category)
        else:
            expenses = Expense.objects.filter(user=user)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Make a mutable copy of the request data for assign the user to the expense 
        data = request.data.copy()   
        # Assign the user to the expense
        data['user'] = request.user.id 
        serializer = ExpenseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
    def get_object(self, expense_id):
        user = self.request.user
        try:
            return Expense.objects.get(id=expense_id, user=user)
        except Expense.DoesNotExist:
            return Response({"message": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, expense_id):
        expense = self.get_object(expense_id)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, expense_id):
        expense = self.get_object(expense_id)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, expense_id):
        expense = self.get_object(expense_id)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)