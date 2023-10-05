from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Device(Model):
    '''
    A DynamoDB Device model
    '''
    class Meta:
        table_name = 'y-alm-devices'
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        host = 'http://localhost:5454'
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
