import requests
def main(dict):
    city=dict["city"]
    q=dict["q"]

    if(city=="caracas"):
        r=requests.get("http://api.openweathermap.org/data/2.5/forecast?q=caracas&APPID=3b31a7e394e41c3a30759dfde1a3383e&units=metric")
    else:
        r=requests.get("http://api.openweathermap.org/data/2.5/forecast?q=madrid&APPID=3b31a7e394e41c3a30759dfde1a3383e&units=metric")

    result=r.json()
    if(q=="weather"):
        op = {"The current weather in {} is":result['list'][0]['weather'][0]['description']}.format(city) ##Aca es donde quiero poner el .format o algo asi
    elif(q=="windy"):
        op = {"The current wind speed is":result['list'][0]['wind']['speed']}
    elif(q=="feels"):
        op = {"It feels like":result['list'][0]['main']['feels_like']}
    elif(q=="temperature"):
        op = {"The temperature is":result['list'][0]['main']['temp']}
    else:
        op = {"ConMiGo got  no answers ConMi":result['list'][0]}
    return op


# return 'Currently, in {}, its {} degrees with {}'.format(city_name, temp, description)