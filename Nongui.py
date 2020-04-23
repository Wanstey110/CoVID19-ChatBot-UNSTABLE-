import random
import matplotlib.pyplot as plt
import requests
import numpy as np
import time
import datetime
from datetime import timedelta
import json

def cUpdate(country):
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
	querystring = {"country": country}
	headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text.find('"confirmed')
	
	toReturn = response.text[result:].replace("}", "")
	toReturn = toReturn.replace("]", "")
	toReturn = toReturn.replace('"', "")
	toReturn = toReturn.replace(',', " ")

    # dRC3 is equal to the number of deaths
	dRC = toReturn.find("s:")
	dRC2 = toReturn.find("recovered")
	dRC3 = int(toReturn[dRC+2:dRC2])

	# cDC3 is equal to the number of cases
	cDC = toReturn.find("d:")
	cDC2 = toReturn.find("deaths")
	cDC3 = int(toReturn[cDC+2:cDC2])

    # cCC2 is equal to the number of recovered
	cCC = toReturn.find('recovered:')
	cCC2 = int(toReturn[cCC+10:])
	mRV = (dRC3 / cDC3) * 100
	mRV = round(mRV, 2)
	mRV2 = f"{round(mRV,2)}% (2dp)"
	
	rRV = (cCC2 / cDC3) * 100
	rRV = f"{round(rRV,2)}% (2dp)"

	"""
	if country == "Sao Tome and Principe":
		cPM = (cDC3 / getPopulation("Sao Tome & Principe"))
		cPM2 = cPM * 1000000
		cPM2 = f"{round(cPM2,2)} (2dp)"	
	else:
		cPM = (cDC3/getPopulation(country))
		cPM2 = cPM * 1000000
		cPM2 = f"{round(cPM2, 2)} (2dp)"
	"""
	return f"Stats:\nConfirmed: {cDC3}\nDeaths: {dRC3}\nRecovered: {cCC2}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}"


def cUpdateWorld():
	url = "https://covid-19-tracking.p.rapidapi.com/v1"
	headers = {
        'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
    }
	response = requests.request("GET", url, headers=headers)
	r = json.loads(response.text)
	cases = int(r[0]["Total Cases_text"].replace(",", ""))
	deaths = int(r[0]["Total Deaths_text"].replace(",", ""))
	recovered = int(r[0]["Total Recovered_text"].replace(",", ""))
	
	mortalityRate = (deaths / cases) * 100
	mortalityRate = f"{round(mortalityRate,2)}% (2dp)"

	recoveryRate = (recovered / cases) * 100
	recoveryRate = f"{round(recoveryRate,2)}% (2dp)"

	"""
	casesperm = (cases / getPopWorld())
	casesperm = casesperm * 1000000
	casesperm = f"{round(casesperm, 2)} (2dp)"
	"""
	return f"Stats:\nConfirmed: {cases}\nDeaths: {deaths}\nRecovered: {recovered}\nMortality Rate:{mortalityRate}\nRecovery Rate:{recoveryRate}"


def cUpdateSpecial(country):
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
	headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
	}
	response = requests.request("GET", url, headers=headers)
	r = response.text
	r2 = json.loads(r)

	if country == "usa" or country == "us" or country == "america":
        # USA
		casesUSA = int(r2["countries_stat"][000]["cases"].replace(",", ""))
		deathsUSA = int(r2["countries_stat"][000]["deaths"].replace(",", ""))
		recoveredUSA = int(r2["countries_stat"][000]
                           ["total_recovered"].replace(",", ""))

		mortalityRateUSA = (deathsUSA / casesUSA) * 100
		mortalityRateUSA = f"{round(mortalityRateUSA,2)}% (2dp)"

		recoveryRateUSA = (recoveredUSA / casesUSA) * 100
		recoveryRateUSA = f"{round(recoveryRateUSA,2)}% (2dp)"

		"""
		casespermUSA = (casesUSA/getPopulation("United States"))
		casespermUSA = casespermUSA * 1000000
		casespermUSA = f"{round(casespermUSA, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesUSA}\nDeaths: {deathsUSA}\nRecovered: {recoveredUSA}\nMortality Rate:{mortalityRateUSA}\nRecovery Rate:{recoveryRateUSA}"

	elif country == "china":
		casesChi = int(r2["countries_stat"][6]["cases"].replace(",", ""))
		deathsChi = int(r2["countries_stat"][6]["deaths"].replace(",", ""))
		recoveredChi = int(r2["countries_stat"][6]
                           ["total_recovered"].replace(",", ""))

		mortalityRateChi = (deathsChi / casesChi) * 100
		mortalityRateChi = f"{round(mortalityRateChi,2)}% (2dp)"

		recoveryRateChi = (recoveredChi / casesChi) * 100
		recoveryRateChi = f"{round(recoveryRateChi,2)}% (2dp)"

		"""
		casespermChi = (casesChi/getPopulation("China"))
		casespermChi = casespermChi * 1000000
		casespermChi = f"{round(casespermChi, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesChi}\nDeaths: {deathsChi}\nRecovered: {recoveredChi}\nMortality Rate:{mortalityRateChi}\nRecovery Rate:{recoveryRateChi}"

	elif country == "canada":
		# Canada
		casesCan = int(r2["countries_stat"][12]["cases"].replace(",", ""))
		deathsCan = int(r2["countries_stat"][12]["deaths"].replace(",", ""))
		recoveredCan = int(r2["countries_stat"][12]
                           ["total_recovered"].replace(",", ""))

		mortalityRateCan = (deathsCan / casesCan) * 100
		mortalityRateCan = f"{round(mortalityRateCan,2)}% (2dp)"

		recoveryRateCan = (recoveredCan / casesCan) * 100
		recoveryRateCan = f"{round(recoveryRateCan,2)}% (2dp)"
		
		"""
		casespermCan = (casesCan/getPopulation("Canada"))
		casespermCan = casespermCan * 1000000
		casespermCan = f"{round(casespermCan, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesCan}\nDeaths: {deathsCan}\nRecovered: {recoveredCan}\nMortality Rate:{mortalityRateCan}\nRecovery Rate:{recoveryRateCan}"
	
	elif country == "france":
		casesFran = int(r2["countries_stat"][4]["cases"].replace(",",""))
		deathsFran = int(r2["countries_stat"][4]["deaths"].replace(",",""))
		recoveredFran = int(r2["countries_stat"][4]["total_recovered"].replace(",",""))

		mortalityRateFran = f"{round((deathsFran / casesFran) * 100,2)}% (2dp)"
		recoveryRateFran = f"{round((recoveredFran / casesFran) * 100,2)}% (2dp)"
		
		"""
		casespermFran = (casesFran / getPopulation("France")) * 100000
		casespermFran = f"{round(casespermFran, 2)}% (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesFran}\nDeaths: {deathsFran}\nRecovered: {recoveredFran}\nMortality Rate:{mortalityRateFran}\nRecovery Rate:{recoveryRateFran}"
		
	elif country == 'england' or country == 'uk' or country == 'britain' or country == 'greatbritain' or country == 'unitedkingdom':
		casesUK = int(r2["countries_stat"][6]["cases"].replace(",", ""))
		deathsUK = int(r2["countries_stat"][6]["deaths"].replace(",", ""))
		recoveredUK = int(r2["countries_stat"][6]["total_recovered"].replace(",", ""))
		
		mortalityRateUK = (deathsUK / casesUK) * 100
		mortalityRateUK = f"{round(mortalityRateUK,2)}% (2dp)"
		
		recoveryRateUK = (recoveredUK / casesUK) * 100
		recoveryRateUK = f"{round(recoveryRateUK,2)}% (2dp)"
		
		"""
		casespermUK = (casesUK/getPopulation("United Kingdom"))
		casespermUK = casespermUK * 1000000
		casespermUK = f"{round(casespermUK, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesUK}\nDeaths: {deathsUK}\nRecovered: {recoveredUK}\nMortality Rate:{mortalityRateUK}\nRecovery Rate:{recoveryRateUK}"

	elif country == 'australia':
		casesAus = int(r2["countries_stat"][27]["cases"].replace(",", ""))
		deathsAus = int(r2["countries_stat"][27]["deaths"].replace(",", ""))
		recoveredAus = int(r2["countries_stat"][27]["total_recovered"].replace(",", ""))
		
		mortalityRateAus = (deathsAus / casesAus) * 100
		mortalityRateAus = f"{round(mortalityRateAus,2)}% (2dp)"
		
		recoveryRateAus = (recoveredAus / casesAus) * 100
		recoveryRateAus = f"{round(recoveryRateAus,2)}% (2dp)"
		
		"""
		casespermAus = (casesAus/getPopulation("Australia"))
		casespermAus = casespermAus * 1000000
		casespermAus = f"{round(casespermAus, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesAus}\nDeaths: {deathsAus}\nRecovered: {recoveredAus}\nMortality Rate:{mortalityRateAus}\nRecovery Rate:{recoveryRateAus}"

def cUpdateIndia():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
	}
    response = requests.request("GET", url, headers=headers)
    r = response.text
    r2 = json.loads(r)

    casesInd = int(r2["countries_stat"][20]["cases"].replace(",", ""))
    deathsInd = int(r2["countries_stat"][20]["deaths"].replace(",", ""))
    recoveredInd = int(r2["countries_stat"][20]["total_recovered"].replace(",", ""))

    mortalityRateInd = (deathsInd / casesInd) * 100
    mortalityRateInd = f"{round(mortalityRateInd,2)}% (2dp)"

    return f"Stats:\nConfirmed: {casesInd}\nDeaths: {deathsInd}\nRecovered: {recoveredInd}\nMortality Rate:{mortalityRateInd}\nRecovery Rate: {recoveredInd}"

print("""
Hello! I am your friendly CoVID-19 ChatBot!
-This version of me is a not very colorful, if you want that version you can download it here:
http://tiny.cc/covidbot2020
""")

flag = True
c = 0

dictOfQuestions = {'howareyou?': "I'm fine thanks!", "whatisachatbot?":
                   "A chatbot is a program which you can chat with (like me)!", "whenwereyouborn?": "I was born on April 13th, 2020!", "thanks!": "No Problemo!", "thankyou!": "My Pleasure!", "whatisacoronavirus?": "Coronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19.", "whatisthecoronavirus?": "Coronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome(MERS) and Severe Acute Respiratory Syndrome(SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19.", "whatarethesymptoms?": "The most common symptoms of COVID-19 are fever, tiredness, and dry cough. Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. These symptoms are usually mild and begin gradually. Some people become infected but don�t develop any symptoms and don't feel unwell. Most people (about 80%) recover from the disease without needing special treatment. Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing. Older people, and those with underlying medical problems like high blood pressure, heart problems or diabetes, are more likely to develop serious illness. People with fever, cough and difficulty breathing should seek medical attention.", "howdoescovid-19spread?": "People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person. Other people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth. People can also catch COVID-19 if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets. This is why it is important to stay more than 1 meter (3 feet) away from a person who is sick.","howdoesthecoronavirusspread?":"People can catch COVID-19 from others who have the virus." , "easteregg": "Well done, you've discovered the Easter egg!", "whenwasthefirstcaseofthecoronavirus?": "The first known case was reported back in November 17th of 2019", "whenwasthefirstcaseofthecoronavirus?": "The first known case was reported back in November 17th of 2019", "whenwasthefirstcaseofcovid19?": "The first known case was reported back in November 17th of 2019", 'aretheaffectspermanent?': 'This depends on how severe the symptoms, if you have mild symptoms then most likely no, however if you have sever symptoms then you may experience chronic lung pains.', 'isthereasolution?': 'Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care.', 'isthereavaccine?': 'Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care.', 'isthereacure?': 'Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care.', 'isthereavaccineforcoronavirus?':'Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care.'}

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
    
    plt.xlabel('Days')
    plt.ylabel('Cases')
    if country == 'us':
        capcountry3 = 'U.S.A.'
    elif ' ' in country:
        capcountry1 = ord(country[0])-32
        capcountry2 = chr(capcountry1)
        capcountry3 = country.replace(country[0], capcountry2)
        for i in range(country.count(" ")):
            capcountry4 = country.find(' ')
            capcountry5 = ord(country[capcountry4])
            capcountry6 = chr(capcountry5)
            capcountry3 = country.replace(country[capcountry4], capcountry6)
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
    
    plt.xlabel('Days')
    plt.ylabel('Death')
    if country == 'us':
        capcountry3 = 'U.S.A.'
    elif ' ' in country:
        capcountry1 = ord(country[0])-32
        capcountry2 = chr(capcountry1)
        capcountry3 = country.replace(country[0], capcountry2)
        for i in range(country.count(" ")):
            capcountry4 = country.find(' ')
            capcountry5 = ord(country[capcountry4])
            capcountry6 = chr(capcountry5)
            capcountry3 = country.replace(country[capcountry4], capcountry6)
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

    if (chat[0] == 'w' or chat[0] == 'h' or chat[0] == 'i' or chat[0] == 'a') and chat[len(chat)-1] != '?':
        chat += "?"

    if chat == 'groupmembers' or chat == 'group' or chat == 'developers' or chat == 'groupmember':
        answer = "William Anstey \n Demetrios Economou"

    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end':
        flag = False

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
        answer = cUpdateWorld()

    elif chat == 'updataustralia' or chat == 'updateusa' or chat == 'updatecanada' or chat == 'updatechina' or chat == 'updateamerica' or chat == 'updateus' or chat == 'updateengland' or chat == 'updateuk' or chat == 'updatebritain' or chat == 'updategreatbritain' or chat == 'updateunitedkingdom' or chat == "updatefrance":
        specialChat = chat.replace("update", "")
        answer = cUpdateSpecial(specialChat)
    elif chat == 'updateindia':
        answer = cUpdateIndia()

    elif chat == 'updatenewzealand':
        answer = cUpdate("New Zealand")

    elif chat == 'updatebosinaandherzegovina' or chat == 'updatebosina':
        answer = cUpdate('Bosnia and Herzegovina')

    elif chat == 'updateczechrepublic':
        answer = cUpdate('Czechia')

    elif chat == 'updatesanmarino':
        answer = cUpdate('San Marino')

    elif chat == 'updatevatican' or chat == 'updatevaticancity':
        answer = cUpdate('Vatican City')

    elif chat == 'updatecostarica':
        answer = cUpdate('Costa Rica')

    elif chat == 'updatedominicanrepublic':
        answer = cUpdate('Dominican Republic')

    elif chat == 'updateelsalvador':
        answer = cUpdate('El Salvador')

    elif chat == "updatecoted'ivoire" or chat == "updatecotedivoire":
        answer = cUpdate("Cote d'Ivoire")

    elif chat == "updatesaotomeandprincipe" or chat == 'saotome&principe':
        answer = cUpdate("Sao Tome and Principe")

    elif chat == "updatesierraleone":
        answer = cUpdate("Sierra Leone")

    elif chat == "updatesouthafrica":
        answer = cUpdate("South Africa")

    elif chat == "updatecentralafricanrepublic":
        answer = cUpdate("Central African Republic")

    elif chat == "updatetrinidad" or chat == "updatetrinidadandtobago" or chat == "updatetobago":
        answer = cUpdate("Trinidad and Tobago")

    elif chat == "updatesouthkorea" or chat == "updates.korea" or chat == "updatekorea,south":
        answer = cUpdate("Korea, South")

    elif chat == "updatesouthsudan":
        answer = cUpdate("South Sudan")

    elif chat == "updatesrilanka":
        answer = cUpdate("Sri Lanka")

    elif chat == "updateuae" or chat == "updateunitedarabemirates" or chat == "updateemirates":
        answer = cUpdate("United Arab Emirates")

    elif chat == "updatesaudiarabia" or chat == "updatearabia" or chat == "updatesaudi":
        answer = cUpdate("Saudi Arabia")

    elif chat == "updateequatorialguinea":
        answer = cUpdate("Equatorial Guinea")

    elif 'update' in chat:
        upc = chat.find('update')
        upc = chat.replace('update', '')
        ascii1 = ord(upc[0])
        ascii2 = chr(ascii1-32)
        rep = upc.replace(upc[0], ascii2)
        answer = cUpdate(rep)

    elif chat == "sympcheck" or chat == "symptomcheck" or chat == "symptomchecker" or chat == "symptomschecker":
        toPrint = sympcheck()
        answer = toPrint

    elif chat == "exit":
      flag = False
    elif 'growthrate' in chat:
      chat = chat.replace('growthrate', '')
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
          graph(chat)

    elif 'deathrate' in chat:
        chat = chat.replace('deathrate', '')
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
            death(chat)
    
    elif chat in dictOfQuestions:
        answer = dictOfQuestions[chat]

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
    try:
        print(answer)
    except:
        print("")
    c += 1