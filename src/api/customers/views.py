from rest_framework import viewsets, status
from rest_framework.response import Response

from src.core.models import Customer
from src.core.forms import CustomerForm
from src.api.customers.serializers import CustomerSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = Customer.objects.all()
        phone = self.request.query_params.get('phone', None)
        if phone is not None:
            queryset = queryset.filter(phone__startswith=phone)
        return queryset

    def create(self, request, *args, **kwargs):
        form = CustomerForm(request.data)
        if form.is_valid():
            form.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        return
