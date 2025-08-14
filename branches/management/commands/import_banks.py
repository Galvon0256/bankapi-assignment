# branches/management/commands/import_banks.py
import csv
from django.core.management.base import BaseCommand
from branches.models import Bank, Branch
from django.db import transaction

class Command(BaseCommand):
    help = 'Import bank data from CSV'
    
    def handle(self, *args, **options):
        # Use transaction for better performance
        with transaction.atomic():
            # Dictionary to track created banks
            Branch.objects.all().delete()
            Bank.objects.all().delete()
            created_banks = {}
            
            # Open file with explicit UTF-8 encoding
            with open('branches/data/banks.csv', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                branches_to_create = []
                
                for row in reader:
                    bank_id = row['bank_id']
                    bank_name = row['bank_name']
                    
                    # Create bank if not exists
                    if bank_id not in created_banks:
                        bank, created = Bank.objects.get_or_create(
                            id=bank_id,
                            defaults={'name': bank_name}
                        )
                        if not created and bank.name != bank_name:
                            bank.name = bank_name
                            bank.save()
                        created_banks[bank_id] = bank
                    
                    # Prepare branch data
                    branches_to_create.append(
                        Branch(
                            ifsc=row['ifsc'],
                            bank=created_banks[bank_id],
                            branch=row['branch'],
                            address=row['address'],
                            city=row['city'],
                            district=row['district'],
                            state=row['state']
                        )
                    )
                
                # Bulk create branches for better performance
                Branch.objects.bulk_create(branches_to_create, batch_size=1000)
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully imported {len(created_banks)} banks and {len(branches_to_create)} branches'
        ))