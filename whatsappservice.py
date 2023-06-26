import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAkWxxB35h4BAKSVlxhUaOh8TZBmvilf8ePAOOFEyOCIa2yx33ZBzZBWKshZAx4Kygt0TJPV4BbnYbLSn5YOPgIKytG5T18ocNK5pyOf8yieTcxjgEO6kpclXNUtG1l9teEAo5UMILwo3VJIFXHBgYPbFuyUu3uP3bYEjpUfUrMR2sLjkiQo"
        api_url = "https://graph.facebook.com/v17.0/107197942400428/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers= headers)

        if response.status_code == 200:
            return True
        return False
    except Exception as exception:
        print(exception)
        return False