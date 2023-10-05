import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Device(Model):
    '''
    A DynamoDB Device model
    '''
    class Meta:
        table_name = os.getenv('DB_TABLE')
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        if(os.getenv('STAGE') == 'dev'):
            host = os.getenv('DYNAMODB_LOCAL_ENDPOINT')
        # Specifies the write capacity
        write_capacity_units = 2
        # Specifies the read capacity
        read_capacity_units = 5
        # Specifies the region
        region = 'eu-north-1'
        
    id = UnicodeAttribute(hash_key=True)
    deviceModel = UnicodeAttribute()
    name = UnicodeAttribute()
    note = UnicodeAttribute()
    serial = UnicodeAttribute()

    def __str__(self):
        return self.deviceModel
