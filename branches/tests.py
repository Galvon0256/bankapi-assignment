from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Bank, Branch
import json

class BankAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data that will be used for all tests
        cls.bank = Bank.objects.create(id=60, name="Test Bank")
        cls.branch = Branch.objects.create(
            ifsc="TEST0000001",
            bank=cls.bank,
            branch="Test Branch",
            address="Test Address",
            city="Test City",
            district="Test District",
            state="Test State"
        )
        cls.client = APIClient()
    
    def test_bank_list(self):
        url = reverse('bank-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Bank")
    
    def test_branch_detail(self):
        url = reverse('branch-detail', args=['TEST0000001'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['branch'], "Test Branch")
        self.assertEqual(response.data['bank']['name'], "Test Bank")
    
    def test_nonexistent_branch(self):
        url = reverse('branch-detail', args=['INVALID_IFSC'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_bank_branches_list(self):
        url = reverse('bank-branches', args=[60])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['ifsc'], "TEST0000001")
    
    def test_bank_branches_filtering(self):
    # Test filtering by city
        url = reverse('bank-branches', args=[60]) + "?city=Test City"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        
        # Test filtering by non-existent city
        url = reverse('bank-branches', args=[60]) + "?city=NonExistent"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)

    def test_bank_branches_search(self):
        # Test search by branch name
        url = reverse('bank-branches', args=[60]) + "?search=Test"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

class ModelTests(TestCase):
    def test_bank_str_representation(self):
        bank = Bank.objects.create(name="Test Bank")
        self.assertEqual(str(bank), "Test Bank")
    
    def test_branch_str_representation(self):
        bank = Bank.objects.create(name="Test Bank")
        branch = Branch.objects.create(
            ifsc="TEST0000001",
            bank=bank,
            branch="Test Branch"
        )
        self.assertEqual(str(branch), "Test Branch (TEST0000001)")

