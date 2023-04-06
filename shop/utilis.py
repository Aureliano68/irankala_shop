import random
import os
from  uuid import uuid4
def create_random_code(count):
    count-=1
    return random.randint(10**count,10**(count+1)-1)

# -----------------------------------------------------------------------------------------------------------
def send_sms(mobilenumber,message):
    pass
    # try:
    #     api = KavenegarAPI('7445704672334F2F47704B4E766C6D64443453776939616664484136797A4B704C5A305557714B754672453D')
    #     params = { 'sender' : '', 'receptor':mobilenumber , 'message' :message}
    #     response = api.sms_send(params)
    #     return response
    # except APIException as error:
    #     print(f'error is :{error}')
    # except HTTPException as error:
    #     print(error)
    
# -----------------------------------------------------------------------------------------------------------
class FileUpload:
    def __init__(self,dir,perfix):
        self.dir=dir
        self.perfix=perfix
        
    def imageupload(self,inctance,filename):
        filename,ext=os.path.splitext(filename)
        return f'{self.dir}/{self.perfix}/{uuid4()}{ext}'
    
# -----------------------------------------------------------------------------------------------------------
def price_by_delivery_tax(price,discount=0):
        delivery=30000
        if price>1000000:
            delivery=0
        tax=(price+delivery)*.09
        sum=price+delivery+tax
        sum=sum-(sum*discount/100)
        return int(sum),delivery,int(tax)
