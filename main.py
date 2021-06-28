import time
import requests
import json



print ("""
WELCOME TO WELEAK INFO BOT
MADE BY INCLUDE#0001 ON DISCORD
discord.gg/oh

Please Type "start" To Start The Bot !
""")
weleak = input('what would you like to do: ')
if weleak == ("start"):
    aInput2 = input ("Please Input Your Weleak Key: ")
    aInput1 = input("Please Input The Email You Would Like To Weleak: ")

    c = requests.get(f"https://api.weleakinfo.to/api?value={aInput1}&type=email&key={aInput2}")
    data = json.loads(c.text)

    weleak1 = data
    print(f'The Password Of The Email Are {weleak1}.')

    time.sleep(16)


main()
