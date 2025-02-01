from vonage import Vonage, Auth, HttpClientOptions
from vonage_sms import SmsMessage, SmsResponse
from settings import API_KEY,API_HOST,API_SECRET,FROM


def send_sms_service(to: str, message: str):
    auth = Auth(api_key=API_KEY, api_secret=API_SECRET)

    options = HttpClientOptions(api_host=API_HOST, timeout=30)

    vonage = Vonage(auth=auth, http_client_options=options)

    message = SmsMessage(to=to, from_=FROM, text=message)
    response = vonage.sms.send(message)
    return response

