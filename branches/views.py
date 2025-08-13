from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankList(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchDetail(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'

class BankBranchesList(generics.ListAPIView):
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city', 'district', 'state']
    search_fields = ['branch', 'address']
    
    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        return Branch.objects.filter(bank_id=bank_id)