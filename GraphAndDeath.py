import random
import matplotlib.pyplot as plt
import requests
import numpy as np
import time
import datetime
from datetime import timedelta
import numpy as np

print("""
Hello! I am your friendly CoVID-19 ChatBot!
-This version of me is a not very colorful, if you want that version you can download it here:
http://tiny.cc/covidbot2020
""")

flag = True
c = 0
def graph(country):
    gdate = str(time.strftime(r"%m-%d-%Y", time.localtime()))
    dm1 = f'{gdate[3]}{gdate[4]}'
    dm2 = str((int(dm1))-1)
    gdate = gdate.replace(dm1, dm2)
    sdate = ('01-22-2020')
    gdate2 = datetime.date.today()
    gdate3 = datetime.date(2020, 1, 22)
    dayspass = str(gdate2-gdate3)
    zerotime = dayspass.find('0:00:0')
    numdaypass = dayspass[:zerotime-7]
    numdaypass = (int(numdaypass))
    x = []
    y = []
    for i in range(0, numdaypass):
        g = str(datetime.date(2020, 1, 22) + timedelta(days=i))
        year = f'{g[0]}{g[1]}{g[2]}{g[3]}'
        month = f'{g[5]}{g[6]}'
        date = f'{g[8]}{g[9]}'
        ndate = f'{month}-{date}-{year}'

        url = f"https://covid1910.p.rapidapi.com/data/confirmed/country/{country}/date/{ndate}"
        headers = {
            'x-rapidapi-host': "covid1910.p.rapidapi.com",
            'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"}
        response = requests.request("GET", url, headers=headers)
        rt = response.text
        rt = rt.replace('"', '')
        rt = rt.replace('[', '')
        rt = rt.replace('{', '')
        rt = rt.replace('}', '')
        rt = rt.replace(']', '')
        rt1 = rt.find('med:')
        confirmed = rt[rt1+4:]
        y.append(confirmed)
        x.append(i)

    plt.plot(x, y)
    print(y)
    plt.xlabel('Days')
    plt.ylabel('Cases')
    if country == 'us':
        capcountry3 = 'U.S.A.'
    else:
        capcountry1 = ord(country[0])-32
        capcountry2 = chr(capcountry1)
        capcountry3 = country.replace(country[0], capcountry2)
    plt.title(f'Cases in {capcountry3}')

    plt.yticks(np.arange(min(x), 70, 4.0))

    plt.show()


def death(country):
    gdate = str(time.strftime(r"%m-%d-%Y", time.localtime()))
    dm1 = f'{gdate[3]}{gdate[4]}'
    dm2 = str((int(dm1))-1)
    gdate = gdate.replace(dm1, dm2)
    sdate = ('01-22-2020')
    gdate2 = datetime.date.today()
    gdate3 = datetime.date(2020, 1, 22)
    dayspass = str(gdate2-gdate3)
    zerotime = dayspass.find('0:00:0')
    numdaypass = dayspass[:zerotime-7]
    numdaypass = (int(numdaypass))
    x = []
    y = []
    for i in range(0, numdaypass):
        g = str(datetime.date(2020, 1, 22) + timedelta(days=i))
        year = f'{g[0]}{g[1]}{g[2]}{g[3]}'
        month = f'{g[5]}{g[6]}'
        date = f'{g[8]}{g[9]}'
        ndate = f'{month}-{date}-{year}'

        url = f"https://covid1910.p.rapidapi.com/data/death/country/{country}/date/{ndate}"
        headers = {
            'x-rapidapi-host': "covid1910.p.rapidapi.com",
            'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"}
        response = requests.request("GET", url, headers=headers)
        rt = response.text
        rt = rt.replace('"', '')
        rt = rt.replace('[', '')
        rt = rt.replace('{', '')
        rt = rt.replace('}', '')
        rt = rt.replace(']', '')
        rt1 = rt.find('ath:')
        confirmed = rt[rt1+4:]
        y.append(confirmed)
        x.append(i)

    plt.plot(x, y)
    print(y)
    plt.xlabel('Days')
    plt.ylabel('Death')
    if country == 'us':
        capcountry3 = 'U.S.A.'
    else:
        capcountry1 = ord(country[0])-32
        capcountry2 = chr(capcountry1)
        capcountry3 = country.replace(country[0], capcountry2)
    plt.title(f'Deaths in {capcountry3}')

    plt.yticks(np.arange(min(x), 70, 4.0))

    plt.show()

def sympcheck():
    print("Welcome to the COVID19 symptom checker\nHave you ever experienced these symptoms?")
    symlist = ['Coughing', 'Fever', 'Shortness of breath', 'Sore throat', 'Headache', 'Loss of taste or smell', 'Fatigue',
               'Muscle and/or body aches', 'Runny/stuffy nose', 'Sneezing', 'Itchy, red, watery eyes', 'Itchy and runny nose']
    num = 0
    for i in symlist:
        num += 1
        print(f'{num}. {i}')
    symptoms = input('If yes, please select the symptoms you have been feeling using their number\nSeperate each symptom with a comma.\nIf you do not experience any of these symptoms, type no.\n')
    if symptoms == 'no' or symptoms == 'No':
        return 'You said you have none of these symptoms. You are most likely in a fine condition. Keep in mind this is not a professional diagnosis and consult your doctor if you are feeling very ill '
    cheeseburger = symptoms.split(',')
    print('You have mentioned that you have:')
    clength = len(cheeseburger)
    flag = True
    while flag:
        for i in range(len(cheeseburger)):
            if i == clength - 1:
                print(f'{symlist[int(cheeseburger[i])-1]}.', end='')
            else:
                print(f'{symlist[int(cheeseburger[i])-1]}, ', end='')

        flag = False

    print(' ')
    print()
    if ("1" in cheeseburger and "2" in cheeseburger and "3" in cheeseburger) or ("3" in cheeseburger and ("1" in cheeseburger or "7" in cheeseburger or "8" in cheeseburger)):
        return 'If you are experiencing Fever, Cough, Shortness of breath and/or muscle pain and body aches, these are all symptoms of the coronavirus. If these are mild, try self isolating, while if these are serious, I advise you to go see a doctor immediately.'
    elif "11" not in cheeseburger and "12" not in cheeseburger:
        return 'You may be suffering from the flu. The flu has all the symptoms listed above, except for shortnes for breath, or itchiness. If you are only experiencing sneezing and/or itchiness, chest tightness, or coughing, perhaps you may be alergic or asmatic. Keep in mind this is not a professional diagnosis and consult your doctor if you are feeling very ill.'
    elif "11" in cheeseburger or "12" in cheeseburger:
        return "Don't worry, if you're only experiencing itchy and runny nose and itchy red watery eyes, then you're suffering from an allergy. Sneezing might also be a symptom of it, and constant couging or chest tightness along with the previous symptoms mentioned might mean youre asmatic. Keep in mind this is not a professional diagnosis and consult your doctor if you are feeling very ill."
    else:
        return 'If you are only experiencing sneezing and/or itchiness or chest tightness perhaps you may be alergic or asmatic. The amin symptoms of coronavirus are difficulty breathing, coughing and fever. The main difference with flu is the fact that the coronavirus targets the cells in your lungs, so while flu does not have the symptom of chest tightness and shortness of breath, the coronavirus does. Keep in mind that this is not a professional diagnosis and consult your doctor if you are feeling very ill '


while flag:
    if c == 0:
      print("Try these commmands:\ngrowthrate + your country\ndeathrate + your country\nsymptomscheck\nupdate + your country\nupdateworld\nAlso feel free to ask me any questions you have about the virus, like when was the first case etc.")

    chat = input("->")
    chat = chat.replace(" ", "")
    chat = chat.replace(",", "")
    chat = chat.lower()

    if chat == 'groupmembers' or chat == 'group' or chat == 'developers' or chat == 'groupmember':
        answer = "William Anstey \n Demetrios Economou"

    elif chat == "what'smyname?" or chat == "whatsmyname?" or chat == "whatismyname?" or chat == "whatsmyname" or chat == 'myname?' or chat == 'myname':
        answer = myname

    elif chat == "what'syourname?" or chat == "whatisyourname?" or chat == "whatsyourname?" or chat == "whatsyourname" or chat == 'yourname?' or chat == 'yourname':
        answer = chatbot

    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end':
        answer = 'Bye'

    elif chat == "help":
        answer = """
        Try these commmands:
        growthrate
        symptomscheck
        update + your country
        updateworld
        Also feel free to ask me any questions you have about the virus, like when was the first case etc.
        """

    elif chat == "hello!" or chat == "hello":
        x = random.randint(1, 3)
        if x == 1:
            answer = "Hey there!"
        elif x == 2:
            answer = "Hi!"
        elif x == 3:
            answer = "Heyo"

    elif chat == 'updateworld':
        answer = cUpdates.cUpdateWorld()

    elif chat == 'updataustralia' or chat == 'updateusa' or chat == 'updatecanada' or chat == 'updatechina' or chat == 'updateamerica' or chat == 'updateus' or chat == 'updateengland' or chat == 'updateuk' or chat == 'updatebritain' or chat == 'updategreatbritain' or chat == 'updateunitedkingdom' or chat == "updatefrance":
        specialChat = chat.replace("update", "")
        answer = cUpdates.cUpdateSpecial(specialChat)

    elif chat == 'updatenewzealand':
        answer = cUpdates.cUpdate("New Zealand")

    elif chat == 'updatebosinaandherzegovina' or chat == 'updatebosina':
        answer = cUpdates.cUpdate('Bosnia and Herzegovina')

    elif chat == 'updateczechrepublic':
        answer = cUpdates.cUpdate('Czechia')

    elif chat == 'updatesanmarino':
        answer = cUpdates.cUpdate('San Marino')

    elif chat == 'updatevatican' or chat == 'updatevaticancity':
        answer = cUpdates.cUpdate('Vatican City')

    elif chat == 'updatecostarica':
        answer = cUpdates.cUpdate('Costa Rica')

    elif chat == 'updatedominicanrepublic':
        answer = cUpdates.cUpdate('Dominican Republic')

    elif chat == 'updateelsalvador':
        answer = cUpdates.cUpdate('El Salvador')

    elif chat == "updatecoted'ivoire" or chat == "updatecotedivoire":
        answer = cUpdates.cUpdate("Cote d'Ivoire")

    elif chat == "updatesaotomeandprincipe" or chat == 'saotome&principe':
        answer = cUpdates.cUpdate("Sao Tome and Principe")

    elif chat == "updatesierraleone":
        answer = cUpdates.cUpdate("Sierra Leone")

    elif chat == "updatesouthafrica":
        answer = cUpdates.cUpdate("South Africa")

    elif chat == "updatecentralafricanrepublic":
        answer = cUpdates.cUpdate("Central African Republic")

    elif chat == "updatetrinidad" or chat == "updatetrinidadandtobago" or chat == "updatetobago":
        answer = cUpdates.cUpdate("Trinidad and Tobago")

    elif chat == "updatesouthkorea" or chat == "updates.korea" or chat == "updatekorea,south":
        answer = cUpdates.cUpdate("Korea, South")

    elif chat == "updatesouthsudan":
        answer = cUpdates.cUpdate("South Sudan")

    elif chat == "updatesrilanka":
        answer = cUpdates.cUpdate("Sri Lanka")

    elif chat == "updateuae" or chat == "updateunitedarabemirates" or chat == "updateemirates":
        answer = cUpdates.cUpdate("United Arab Emirates")

    elif chat == "updatesaudiarabia" or chat == "updatearabia" or chat == "updatesaudi":
        answer = cUpdates.cUpdate("Saudi Arabia")

    elif chat == "updateequatorialguinea":
        answer = cUpdates.cUpdate("Equatorial Guinea")

    elif 'update' in chat:
        upc = chat.find('update')
        upc = chat.replace('update', '')
        ascii1 = ord(upc[0])
        ascii2 = chr(ascii1-32)
        rep = upc.replace(upc[0], ascii2)
        answer = cUpdates.cUpdate(rep)

    elif chat == "sympcheck" or chat == "symptomcheck" or chat == "symptomchecker" or chat == "symptomschecker":
        toPrint = sympcheck()
        answer = toPrint

    elif chat == "exit":
      flag = False
    elif 'growthrate' in chat:
      gc = chat.replace('growthrate', '')
      if chat == 'usa' or chat == 'us' or chat == 'u.s.a.' or chat == 'u.s.':
          graph('us')
      elif chat == 'uk' or chat == 'unitedkingdom' or chat == 'u.k.':
          graph('united kingdom')
      elif chat == 'newzealand':
          graph("new zealand")
      elif chat == 'bosinaandherzegovina' or chat == 'bosina':
          graph('bosnia and herzegovina')
      elif chat == 'czechrepublic':
          graph('czechia')
      elif chat == 'sanmarino':
          graph('san marino')
      elif chat == 'vatican' or chat == 'vaticancity':
          graph('vatican city')
      elif chat == 'costarica':
          graph('costa rica')
      elif chat == 'dominicanrepublic':
          graph('dominican republic')
      elif chat == 'elsalvador':
          graph('el salvador')
      elif chat == "coted'ivoire" or chat == "cotedivoire":
          graph("cote d'ivoire")
      elif chat == "saotomeandprincipe" or chat == 'saotome&principe':
          graph("sao tome and principe")
      elif chat == "sierraleone":
          graph("sierra leone")
      elif chat == "southafrica":
          graph("south africa")
      elif chat == "centralafricanrepublic":
          graph("central african republic")
      elif chat == "trinidad" or chat == "trinidadandtobago" or chat == "tobago":
          graph("trinidad and tobago")
      elif chat == "southkorea" or chat == "s.korea" or chat == "korea,south":
          graph("korea, south")
      elif chat == "southsudan":
          graph("south sudan")
      elif chat == "srilanka":
          graph("sri lanka")
      elif chat == "uae" or chat == "unitedarabemirates" or chat == "emirates":
          graph("united arab emirates")
      elif chat == "saudiarabia" or chat == "arabia" or chat == "saudi":
          graph("saudi arabia")
      elif chat == "equatorialguinea":
          graph("equatorial guinea")
      else:
          graph(gc)

    elif 'deathrate' in chat:
        gc = chat.replace('deathrate', '')
        if chat == 'usa' or chat == 'us' or chat == 'u.s.a.' or chat == 'u.s.':
            death('us')
        elif chat == 'uk' or chat == 'unitedkingdom' or chat == 'u.k.':
            death('united kingdom')
        elif chat == 'newzealand':
            death("new zealand")
        elif chat == 'bosinaandherzegovina' or chat == 'bosina':
            death('bosnia and herzegovina')
        elif chat == 'czechrepublic':
            death('czechia')
        elif chat == 'sanmarino':
            death('san marino')
        elif chat == 'vatican' or chat == 'vaticancity':
            death('vatican city')
        elif chat == 'costarica':
            death('costa rica')
        elif chat == 'dominicanrepublic':
            death('dominican republic')
        elif chat == 'elsalvador':
            death('el salvador')
        elif chat == "coted'ivoire" or chat == "cotedivoire":
            death("cote d'ivoire")
        elif chat == "saotomeandprincipe" or chat == 'saotome&principe':
            death("sao tome and principe")
        elif chat == "sierraleone":
            death("sierra leone")
        elif chat == "southafrica":
            death("south africa")
        elif chat == "centralafricanrepublic":
            death("central african republic")
        elif chat == "trinidad" or chat == "trinidadandtobago" or chat == "tobago":
            death("trinidad and tobago")
        elif chat == "southkorea" or chat == "s.korea" or chat == "korea,south":
            death("korea, south")
        elif chat == "southsudan":
            death("south sudan")
        elif chat == "srilanka":
            death("sri lanka")
        elif chat == "uae" or chat == "unitedarabemirates" or chat == "emirates":
            death("united arab emirates")
        elif chat == "saudiarabia" or chat == "arabia" or chat == "saudi":
            death("saudi arabia")
        elif chat == "equatorialguinea":
            death("equatorial guinea")
        else:
            death(gc)
    else:
      blurb = random.randint(1, 4)
      if blurb == 1:
          answer = "I see"
      elif blurb == 2:
          answer = "Interesting"
      elif blurb == 3:
          answer = "Indeed"
      elif blurb == 4:
          answer = "I comprehend"
      elif chat.endswith("?"):
          answer = "I'm sorry but I can't answer that"
    print(answer)
    c += 1
