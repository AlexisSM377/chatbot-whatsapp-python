def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message ["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else:
        print("sin mensaje")

    return text

def TextMessage(text,number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": text
            }
        } 
    return data

def TextFormatMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "*Bienvenido al Chat Bot de BIT Tecnologies*\n_Necesitas enviar tu correo_\n~Pero tiene que estar~\n```en diferente formato```"
            }
        }
    return data

def ImageMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "image",
            "image": {
                "link": "https://ibb.co/0BwT9B8"
            }
        }
    return data

def AudioMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "audio",
            "audio": {
                "link": "http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/theme_01.mp3"
            }
        }
    return data

def VideoMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "video",
            "video": {
                "link": "https://mylivewallpapers.com/games/fire-keeper-dark-souls-3-live-wallpaper-2.mp3"
            }
        }
    return data

def DocumentMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "document",
            "document": {
                "link": "https://www.faq.cat/wp-content/uploads/2017/08/2_guia_menorca.pdf"
            }
        }
    return data

def LocationMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "location",
            "location":{
                "latitude":"19.26088018198212 ",
                "longitude":"-99.56426857746598",
                "name":"BIT TECNOLOGIES",
                "address":"C. 16 de Septiembre Nte #636, Lazaro Cardenas, 52148 Metepec, Méx."
            }
        }
    return data

def ButtonsMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive":{
                "type":"button",
                "body": {
                    "text":"¿Confirmas tu registro?"
                },
                "action": {
                    "buttons":[
                        {
                            "type":"reply",
                            "reply": {
                                "id": "001",
                                "title": "Correcto,Quiero unirme a BIT"
                            }
                        },
                        {
                            "type":"reply",
                            "reply": {
                                "id":"002",
                                "title":"No busco este servicio"
                            }
                        }
                    ]
                }
            }
        }
    return data

def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ I have these options"
        },
        "footer": {
            "text": "Select an option"
        },
        "action": {
            "button": "See options",
            "sections": [
                {
                    "title": "Buy and sell products",
                    "rows": [
                        {
                            "id": "main-buy",
                            "title": "Buy",
                            "description": "Buy the best product your home"
                        },
                        {
                            "id": "main-sell",
                            "title": "Sell",
                            "description": "Sell your products"
                        }
                    ]
                },
                {
                    "title": "📍center of attention",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agency",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contact center",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    }
}
    return data