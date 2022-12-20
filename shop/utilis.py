import random

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
