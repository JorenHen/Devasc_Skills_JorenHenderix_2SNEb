# LAB 1 - Python experiments

## Part 1: Install different tools/packages on Ubuntu DEVASC-LABVM
- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

### Taak voorbereiding en implementatie

1. Installeren van de DEVASC-LABVM
2. Update en upgrade van apt om errors tegen te gaan: `sudo apt update && sudo apt upgrade`
3. Installeren van Pythone en PIP: `sudo apt install python3 python3-pip`
4. Installeren van Visual Studio Code: `sudo snap install --classic code`
5. Jupiter Notebook installeren: `sudo pip3 install jupyter`
6. Python IDLE installeren: `sudo apt install idle3`

### Taak troubleshooting

Door het uitvoeren van `sudo apt update && sudo apt upgrade` voorkomen we errors bij het installeren van applicaties.

### Taak verifieren 

[Installed verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%201.png)

[Jupyter werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%202.png)

[IDLE werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%203.png)


<br></br>


## Part 2: Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (Part 1)

- timedate.py
- geopy-geocoders_location.py
- location.py

### Taak voorbereiding en implementatie

1. Repository kopieren: `git clone https://github.com/wleppens/PythonExperiments`
2. Scripts uitvoeren: `python3 <script>.py`

### Taak troubleshooting

- Module Folium niet gevonden: `pip3 install folium`
- Module Geopy niet govonden: `pip3 install geopy`

### Taak verifieren

[Scripts uitvoeringen verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%204.png)


<br></br>


## Part 3: Install different tools/packages on Windows OS (deep dive exercise) ++

- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

Investigate the compatibility of the tools with Windows OS and explain briefly if necessary.

### Taak voorbereiding en implementatie

1. Download Python met de installer voor Windows (x86 executable installer) van: https://python.org
2. Dowload Visual Studio 2022: https://visualstudio.microsoft.com/downloads/
3. Download Jupyter: `pip install jupyter`
4. download IDLE: `pip install idle`

### Taak troubleshooting

Als Jupyter Notebook een error geeft tijdens het installeren probeer

- Pip te upgraden: `python -m pip install --upgrade pip`

En daarna Jupyter opnieuw proberen te installeren 

Als Jupyter nogsteeds niet werkt:

- Open Jupyter Notebook met dit commando: `python -m notebook`

### Taak verifieren

[Installed verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%205.png)

[IDLE install verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%206.png)

[IDLE werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%207.png)

[Jupyter werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%208.png)


<br></br>


## Part 4: Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++

- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

### Taak voorbereiding en implementatie

- Installeer Ubuntu 22.04.1 ISO via: https://old-releases.ubuntu.com/releases/22.04.1/
- Installeer de VM

1. Update en upgrade apt om errors te voorkomen `sudo apt update` `sudo apt upgrade`
2. installeer Snap voor visual studio code `sudo apt install snapd` 
3. Installeer Visiual Studio Code `Sudo snap install --classic code`
4. installeer Python en pip `sudo apt intall python3` `sudo apt install python3-pip`
5. Installeer jupyter `sudo apt install jupyter`
6. installeer IDLE `sudo apt install idle`

### Taak troubleshooting

### Taak verifieren

[Install verificaties](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%209.png)

[Jupyter werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%2010.png)

[IDLE werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%2011.png)


<br></br>


# LAB 2 - Explore Rest APIs With API Simulator And Postman.

## Part 1: Explore API Documentation Using the API Simulator

- DEVASCVM
- library.demo.local
- curl

### Taak voorbereiding en implementatie

#### API call via de GUI

1. Surfen naar library.demo.local
2. Naar de "Our Books" tab gaan
3. Op de knop `Click here for API docs` drukken
4. Ga dan naar Get\Books
5. Daarna "Try it out"
6. Op de knop `Execute` drukken

#### API call via curl en API key

- API call met curl doen we aan de hand van dit commando: 

`curl -X get "http://library.demo.local/api/v1/books?includeISBN=true" -H accept: application/json`

#### POST call voor API key

1. DEVASCVM opstarten
2. Surfen naar library.demo.local
3. Naar de "Our Books" tab gaan
4. Op de knop `Click here for API docs` drukken
5. Ga dan naar POST\LoginViaBasic
6. Daarna "Try it out"
7. Op de knop `Execute` drukken

#### Delete book using curl and API key

`curl -X DELETE "http://library.demo.local/api/v1/books/4" -H "accept: application/json" -H "X-API-KEY:cisco|GlKfOH9DXGl3CZHtyQLh4E25lavAw_EB0W5WrxfKBBk"`

### Taak troubleshooting

Ik heb geen problemen gehad tijdens deze task
Maar moest u problemen krijgen probeer dan 

- `sudo apt update`
- `sudo apt upgrade`
- `sudo reboot now`

### Taak verifieren 

Naar Our Books gaan via deze knop [klik hier](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/Klik%20hier.png)

Get Books uitvoeren via [GUI API Call](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/Get%20books.png) [uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/execute.png)

[Inloggen voor POST via GUI](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/Post%20login%20voor%20key.png)
Gekregen [Key](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/POST%20GUI%20uitvoer.png)

API Call cia [Curl](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/Curl%20succes.png)

API call [DELETE met curl](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/CURL%20delete%20met%20API%20key.png)


<br></br>


## Part 2: Use Postman to Make API Calls to the API Simulator

- DEVASCVM
- Postman
- library.demo.local

### Taak voorbereiding en implementatie

1. DEVASCVM opstarten
2. Open Postman op het bureublad van de DEVASCVM
3. POST request maken naar `http://library.demo.local/api/v1/LoginViaBasic`
4. Autorization tab openen
5. Basic Auth selecteren
6. Username en password invullen `cisco` `Cisco123!`
7. Op send drukken
8. POST request maken naar `http://library.demo.local/api/v1/books`
9. Bij Authorization API Key selecteren
10. Key values ingeven `X-API-KEY` `cisco|0DOEZlctzTiAKVOG5_z2Io1Be3ugxk84UBCsn6coPWg`
11. Op send drukken
12. Overige GET en POSTs uitvoeren

### Taak troubleshooting

Ik had geen problemen tijdens deze taak.
Moest u wel problemen hebben:

- Herstart Postman 
- Herstart DEVASC Machine `sudo reboot now`

### Taak verifieren 

We krijgen de token binnen in de body van de request [verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%202/POST%20request%20succes.png)

[Post naar /books via postman](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%202/POST%20naar%20books.png)

[Post uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%202/POST%20succes.png)


<br></br>


## Part 3: Use Python to Add 100 Books to the API Simulator

- DEVASCVM
- Visual Studio Code
- Netacad

### Taak voorbereiding en implementatie

1. DEVASCVM opstarten
2. Visual Studio Code openen
3. Script maken via de LAB van NetAcad Devasc

Het script is opgedeeld in verschillende delen op Devasc

- Faker
```
{
 python3
 from faker import Faker
 fake = Faker()
 print('My name is {}.'.format(fake.name()))
 print('My name is {0} and i wrote {1} ({2})'.format(fake.name(),fake.catch_phrase(),fake.isbn13()))
}
``` 

- For loop
```
{
 for i in range (10):
     print(fake.name())
}
```

Alle delen van het script (te vinden op netacad) zijn samengevoegd in het [script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%203/Add100RandomBooks.py)

### Taak troubleshooting

Ik had geen problemen tijdens deze taak.
Moest u wel problemen hebben:

- Herstart Visual Studio Code
- `sudo apt update`
- `sudo apt upgrade` 
- Herstart DEVASC Machine

### Taak verifieren 

[Script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%203/Add100RandomBooks.py)

[Uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%203/Script%20uitvoer.png)


<br></br>


# Lab 3 - Python Review - Development tools and Classes
## Part 1: Python Programming Review

- DEVASCVM
- Python3
- Visual Studio Code

### Taak voorbereiding en implementatie

1. DEVASCVM opstarten
2. Visual Studio Code opstarten
3. Scriptjes maken in Visual Studio Code

### Taak troubleshooting

Ik heb geen problemen ervaren. Moest u wel problemen ervaren probeer dan:
- `sudo apt update`
- `sudo apt upgrade`
- Visual Studio Code herstarten

Of

- `sudo reboow now`

### Taak verifieren 

Script 1: [Hello World](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/HelloWorld.py)

```
{
print("Hello World!");
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/HelloWorldUitvoer.png)


Script 2: [VLAN](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/VLAN.py)

```
{
nativeVLAN = 1;
dataVLAN = 100;

if nativeVLAN == dataVLAN:
    print("De native en data VLANs zijn het zelfde.");

else:
    print("De native en data VLANs zijn verschillend.");
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/VLANuitvoer.png)


Script 3: [Persoonlijk](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/Persoonlijk.py)

```
{
Naam = input("Wat is jouw naam? ");
Achternaam = input("Wat is jouw achternaam? ");
Locatie = input("Waar woon jij? ");
Leeftijd = input("Hoe oud ben jij? ");
print("Hallo " + Naam + Achternaam + "! U woont in " + Locatie + " en u bent " + Leeftijd + " jaar oud");
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/PersoonlijkUitvoer.png)


Script 4: [Router](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/Router.py)

```
{
Routers=["LAB-RA08-Router01", "LAB-RA08-Router02", "LAB-RA08-Router03"];
for Device in Routers:
    print(Device);
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/RouterUitvoer.png)


Script 5: [TellenTot](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/TellenTot.py)

```
{
Eindgetal = input("Geef een nummer tot waar de teller moet lopen: ");
Eindgetal = int(Eindgetal);
Beginwaarde = 1
while Beginwaarde <= Eindgetal:
    print(Beginwaarde)
    Beginwaarde = Beginwaarde + 1;
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/TellenTotUitvoer.png)


Script 6: [IPV4 ACL](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/IPV4%20ACL.py)

```
{
ACLnummer = int(input("Wat is het IPv4 ACL nummer? "));
if ACLnummer >= 1 and ACLnummer <= 99:
    print("Dit is een standard IPv4 ACL.");
elif ACLnummer >=100 and ACLnummer <= 199:
    print("Dit is een extended IPv4 ACL.");
else:
    print("Dis is geen standard of extended IPv4 ACL.");
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/IPV4ACLuitvoer.png)


Script 7: [Bestand](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/Bestand.py)

```
{
Bestand = open("test.txt","r");
for item in Bestand:
    print(item);
Bestand.close();
}
```
[uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%201/LAB3%20Task1%20Screenshots/BestandUitvoer.png)


<br></br>


## Part 2: Explore Python Development Tools

- DEVASCVM
- Python3
- Netacad
- pip
- pip3

### Taak voorbereiding en implementatie

- Nakijken op welke python versie we zitten `python3 -V`
- Python3 directory achterhalen `which python3`

### Virtuele omgeving

#### Stap1: Python3 virtuele omgeving maken

1. `cd labs/devnet-src/python/`
2. `python3 -m venv devfun`

[Stap 1 Screenshot](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%201.png)

#### Stap2: Activeren en testen

1. `source devfun/bin/activate`
2. `pip3 freeze`
3. `pip3 install requests`
4. `pip3 freeze`
5. `deactivate`

[Stap 2 Screenshot](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%202.png)

#### Stap3: De huidige geinstalleerde pakketen controlleren

1. `python3 -m pip freeze`
2. `python3 -m pip freeze | grep requests`

[Stap 3 Screenshot](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%203.1.png)
[Stap 3 Screenshot](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%203.2.png)

### Virtuele omgeving delen

1. Virtuele omgeving heractiveren `source devfun/bin/activate`
2. Pip3 uitput wegschrijven naar bestand `pip3 freeze > requirements.txt`
3. `deactivate`
4. `ls`
5. Nieuwe virtuele omgeving maken `python3 -m venv devnew`
6. Pip3 gebruiken om de zelfde requirements te downloaden `pip3 install -r requirements.txt`
7. `pip3 freeze`
8. `deactivate`

### Taak troubleshooting

Ik heb geen problemen gehad met deze taak

Moest u wel problemen hebben probeer dan:
- `sudo apt update`
- `sudo apt upgrade`

of
- `sudo reboot now`

### Taak verifieren 

Virtuele omgeving maken:

[Screenshot stap 1](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%201.png)

[Screenshot stap 2](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%202.png)

[Screenshot stap 3](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%203.1.png)

[Screenshot stap 3](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Stap%203.2.png)

Virtuele omgeving delen:

[Screenshot](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%202/Omgeving%20delen.png)


<br></br>


## Part 3: Explore Python Classes

- DEVASCVM
- Visual Studio Code
- Netacad

### Taak voorbereiding en implementatie

1. DEVASCVM opstarten
2. Visual Studio Code opstarten

#### Functie schrijven: [Script1](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%203/Functie.py)

```
{
def myCity(city):
    print("I live in " + city + ".");
myCity("Austin");
myCity("Tokyo");
myCity("Salzburg");
}
```

#### Class schrijven: [Script2](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%203/Class.py)


```
{
class Location:
    def __init__(self, name, country):
        self.name = name;
        self.country = country;
    def myLocation(self) :
        print("Hi, mijn naam is " + self.name + " en ik woon in " + self.country + ".");
Locatie = Location("Tomas", "Portugal");
Locatie.myLocation();
Locatie2 = Location("Ying", "China");
Locatie3 = Location("Amare", "Kenya");
Locatie2.myLocation();
Locatie3.myLocation();
JouwLocatie = Location("Your_Name", "Your_Country");
JouwLocatie.myLocation();
}
```

### Taak troubleshooting

Ik heb geen problemen gehad met deze taak

Moest u wel problemen hebben probeer dan:
- `sudo apt update`
- `sudo apt upgrade`

of
- `sudo reboot now`

### Taak verifieren 

[Screenshot uitvoer eerste script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%203/LAB3%20Task3%20Screenshots/FunctieUitvoer.png)

[Screenshot uitvoer tweede script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%203%20-%20Python%20revieuw%20-%20Development%20tools%20and%20classes/Task%203/LAB3%20Task3%20Screenshots/ClassUitvoer.png)


<br></br>


# Lab 4 - Network infrastructure and torubleshooting

## Part 1: Network Infrastructure

### Taak voorbereiding en implementatie

- Console kabel
- Cisco Switch
- Cisco Router
- UTP kabels
- Voeding kabels

Router instellen:

- VTY en Console Line instellen
- Poorten en subinterfaces instellen
- OSPF instellen
- DHCP opzetten
- Secutiry toepassen
- Basis configuratie
- Domein aanmaken
- RSA key genereren
- SSH versie 2 aanzetten

Switch insstellen:

- Basis config
- Poorten instellen
- VLANs instellen 
- Security toepassen
- VTY en Console Line instellen

IP plan
| Device          | Interface | VLAN | IP            |
| --------------- | --------- | ---- | ------------- |
| LAB-RACK08-R03  | G0/0.10   | 10   | 172.16.8.4    |
| LAB-RACK08-R03  | G0/0.40   | 40   | 172.16.8.52   |
| LAB-RACK08-R03  | G0/0      |      |               | 
| LAB-RACK08-R03  | G0/1      |      | 10.199.66.108 | 
| LAB-RACK08-SW03 | VLAN10    |  10  | 172.16.8.5    | 
| LAB-RACK08-SW03 | VLAN40    |  40  | 172.16.8.5    | 

connectie maken naar tftp:

- configs aanpassen:
1. Statishe route naar tftp server
2. Uitgaande poort moet ip bereikbaar zijn
3. `copy tftp: running-config` `10.199.64.134` `lab-ra08-DEVICE-confg`

### Taak troubleshooten

- Tftp uitgaande poort aanpassen op de router `ip tftp source-interface GigabitEthernet 0/0.10`
- SSH versie 2 gebruiken en hiervoor een nieuwe rsa key aanmaken `crypto key generate rsa``1028` `ip ssh version 2`

### Taak verificatie

Internet connectiviteit werkt
TFTP naar de server werkte op de switch en router (na het aanpassen van de tftp interface)

[Configuratie Switch](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Config_Switch.txt)

[Configuratie Router](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Config_Router.txt)

[Netwerk tekening](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%204%20-%20Network%20infrastructure%20and%20troubleshooting/Netwerktekening.png)


<br></br>


## Part 2: Network Troubleshooting

- Console kabel
- Cisco Switch
- Cisco Router
- UTP kabels
- Voeding kabels

### Taak voorbereiding en implementatie

- Router instellen (Zie part 1)
- Switch instellen (Zie part 1)

### Taak troubleshooting

- Tftp uitgaande poort aanpassen op de router `ip tftp source-interface GigabitEthernet 0/0.10`
- SSH versie 2 gebruiken en hiervoor een nieuwe rsa key aanmaken `crypto key generate rsa``1028` `ip ssh version 2`
- Default route instellen op router zodat er naar de TFTP server connectie kan gemaakt worden

### Taak verifieren

- Backup van switch en router naar tftp serverm maken
- Backup terughalen van tftp server
- Vanaf laptop SSH verbinding maken met de switch en router


<br></br>


# Lab 5 - Software Development and Design Content

## Part 1 Software Version Control with Git

- DEVASCVM
- GIT
- Github account

### Taak voorbereiding en implementatie

1. DevascVM opstarten
2. Github account aanmaken op de github site
3. Fine-grained personal access token maken

 - Ga naar `Account Settings` op je github
 - `Developer settings`
 - `Personal Acces token` > `Fine grained personal acces code`
 - Alle rechten toekennen op de token zodat we niet in problemen komen met pushen naar github wegens "read only rechten"


#### GIT repository initialiseren 

```
{
git config --global user.name "JorenHen"
git config --global user.email joren.henderix@student.pxl.be
git config --list
mkdir Devask_Skills
cd Devask_Skills/
git init
git pull
}
```

#### Bestanden naar github pushen via GIT

```
{
git remote add origin https://github.com/JorenHen/Devasc_Skills_JH.git
git pull
git add .
git commit -m "Screenshots en scripts toegevoegd"
git push -u origin master
}
```

- GIT gebruikersnaam en Fine-grained personal access token invullen 
- Gewenste bestanden zoals screenshots en scripts toevoegen aan de "Devask_Skills/" directory

#### Bestanden wijzigen via GIT

```
{
cd Devask_Skills/
vim readme.txt
git status
git add readme.txt
git commit -m "Readme file aangepast"
git log
git diff b510f8e 9f5c4c5
}
```

#### Nieuwe branch aanmaken en samenvoegen

```
{
git branch test
git branch
git checkout feature
git branch
git add test.txt
git status
git commit -m "Nieuw bestand toegevoegd aan test branch"
git log
git checkout master
git branch
git merge test
}
```

#### Nieuwe branch verwijderen

```
{
git branch -d test
git branch
}
```

#### Conflicten tijdens het samenvoegen van branches

```
{
git branch test2
git checkout test2
git branch
cat test.txt
sed -i 's/Test/Succes/'
cat test.txt
git commit -a -m "Test veranderd naar Succes voor test2 branch"
git checkout master
git branch
sed -i 's/Test/Succes/' test.txt
cat test.txt
git commit -a -m "Test veranderd naar Failed voor master branch"
git merge test2
git log
cat test.txt
vim test.txt
cat test.txt
git add test.txt
git commit -a -m "Manueel test2 branch samengevoegd"
git log
}
```

### Taak troubleshooten

- Aanmaken van Fine-grained personal access token
- Rechten aanpassen van de peronal acces token wegens Read only problemen tijdens het pushen naar Github

### Taak verifieren 

[Screenshot succesval pushen naar git](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task1%20Screenshots/Git%20push%20succes.png)


<br></br>


## Part 2: Create a Python Unit Test 3.5.7

- DEVASCVM
- Visual Studio Code

### Taak voorbereiden en implementern 

1. DevascVM osptarten
2. Visual Studio Code openen

#### Unittest omgeving leren kennen

- Help commando voor unittest:

`python3 -m unittest -h`

- Python functie testen met unittest

`cd labs/devnet-src/unittest/`
`more unittest/test_data.py`

- json_search funtie maken in Visual Studio Code [Script1](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/recursive_json_search.py) [Script2](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/test_json_search.py)

### Taak troubleshooten

Problemen met uitvoeren van het script (errors)

- Open het script in de unittest directory. Ik had een nieuwe directory gemaakt binnenin mijn Devask_Skills/ map hierdoor werkte het niet.
- `Sudo apt update`
- `Sudo apt upgrade`

### Taak verifieren 

[Screenshot help commando](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task2%20Screenshots/Unittest%20script%20succes.png)


[Screenshot unittest](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task2%20Screenshots/more%20test_data.png)


[Screenshot script uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task2%20Screenshots/Unittest%20script%20succes.png)


<br></br>


## Part 3: Parse Different Data Types with Python Cisco

- DEVASCVM
- Visual Studio Code

### Taak voorbereiden en implementern 

- XML file aanmaken 
- XML.py file aanmaken
- JSON file aanmaken
- JSON.py file aanmaken
- YAML file maken
- YAML.py file maken

### Taak troubleshooten

Geen problemen gehad tijdens deze taak. Moest u wel problemen hebben probeer dan een van de volgende opties:

- `sudo apt update` `sudo apt upgrade`
- `sudo reboot now`

### Taak verifieren 

[XML file](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Scripts/XML/myfile.xml)

[XML script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Scripts/XML/parsexml.py)

[JSON file](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Scripts/JSON/myfile.json)

[JSON script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Scripts/JSON/parsejson.py)

[YAML file](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Scripts/YAML/myfile.yaml)

[YAML script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Scripts/YAML/parseyaml.py)

[Screenshot uitvoer scripts](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%205%20-%20Software%20development%20and%20design%20content/LAB5%20Task3%20Screenshots/Scripts%20uitvoer.png)


<br></br>


# LAB 6 - Python Network automation with netmiko

## Task 1: Connecting to a single iOS device

- Cisco Router en Switch
- DEVASCVM
- Visual Studio Code

### Taak voorbereiding en implementatie

- DEVASCVM opstarten
- Visual Studio Code opstarten
- Scripts maken

### Taak troubleshooting

Ik had geen problemen tijdens deze taak. Moest u wel problemen hebben:

- Controller je router/switch config
- Verifieer of je wel connectie hebt naar de router of switch
- Heb je een RSA key gemaakt op de devices? `crypto key generate rsa` `1028`
- Staat SSH versie 2 aan? `ip ssh version 2`

### Taak verificatie

- Basis van elk script:

```
{
cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.8.",
    "username": "admin",
    "password": "Administrator123."
}
}
```

NOTE: Als je deze script zelf wilt uitvoeren vergeet dan niet de host, username en password waardes aan te passen naar de juiste waardes voor jouw device

- Show commandos uitvoeren

```
{
command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

print(output)
}
```

NOTE: De waarde van de variabele "command" dient aangepast te worden naar het gewenste show commando

- Config commandos uitvoeren

```
{
connection = ConnectHandler(**cisco1)
connection.enable()

commands = ['vlan 100', 'name TEST', 'exit']
connection.send_config_set(commands)

print('Uitgevoerd')
connection.disconnect()
}
```

NOTE: De waarde van de variabele "command" dient aangepast te worden naar het gewenste configuratie commando

[Scripts](https://github.com/JorenHen/Devasc_Skills_JH/tree/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Taak1) getest via DEVASC VM.

<br></br>


## Task 2: Connect to multiple IOS devices

- Cisco Router en Switch
- DEVASCVM
- Visual Studio Code

### Taak voorbereiding en implementatie

- DEVASCVM opstarten
- Visual Studio Code opstarten
- Scripts maken

### Taak troubleshooting

Ik had geen problemen tijdens deze taak. Moest u wel problemen hebben:

- Controller je router/switch config
- Verifieer of je wel connectie hebt naar de router of switch
- Heb je een RSA key gemaakt op de devices? `crypto key generate rsa` `1028`
- Staat SSH versie 2 aan? `ip ssh version 2`

### Taak verificatie

- Basis van elk script:

```
{
devices = [
{ 
    "device_type": "cisco_ios",
    "host": "172.16.8.5",
    "username": "admin",
    "password": "Administrator123."
}
{ 
    "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
}
]
}
```

NOTE: Als je deze script zelf wilt uitvoeren vergeet dan niet de host, username en password waardes aan te passen naar de juiste waardes voor jouw device

- Show commandos uitvoeren

```
{
command = ["show ip int brief","show ip ospf"]
for device in devices:
    net_connect = ConnectHandler(**device)
    for command in commands:
        output = net_connect.send_command(command)
        print(output)

    net_connect.disconnect()
}
```

NOTE: De waarde van de variabele "command" dient aangepast te worden naar het gewenste show commando

- Config commandos uitvoeren

```
{
commands = ['vlan 100', 'name TEST']

for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_config_set(commands)
    print(output)
    print('uitgevoerd')

    connection.disconnect()
}
```

NOTE: De waarde van de variabele "command" dient aangepast te worden naar het gewenste configuratie commando

[Scripts](https://github.com/JorenHen/Devasc_Skills_JH/tree/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Taak2) getest via DEVASC VM.


<br></br>


## Task 3: Connect to IOS-XE devices

- CSR1000v VM
- DEVASCVM
- Visual Studio Code

### Taak voorbereiding en implementatie

- DEVASCVM opstarten
- Visual Studio Code opstarten
- Scripts maken

### Taak troubleshooting

Ik had geen problemen tijdens deze taak. Moest u wel problemen hebben:

- Controller je switch config
- Verifieer of je wel connectie hebt naar de switch
- Heb je een RSA key gemaakt op de devices? `crypto key generate rsa` `1028`
- Staat SSH versie 2 aan? `ip ssh version 2`

### Taak verificatie

- Basis van elk script:

```
{
cisco1 = { 
    "device_type": "cisco_ios",
    "host": "192.168.253.128",
    "username": "cisco",
    "password": "cisco123!"
}
}
```

NOTE: Als je deze script zelf wilt uitvoeren vergeet dan niet de host, username en password waardes aan te passen naar de juiste waardes voor jouw device

- Show commandos uitvoeren

```
{
command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

print(output)
}
```

NOTE: De waarde van de variabele "command" dient aangepast te worden naar het gewenste show commando

- Config commandos uitvoeren

```
{
connection = ConnectHandler(**cisco1)
connection.enable()

commands = ['vlan 100', 'name TEST', 'exit']
connection.send_config_set(commands)

print('Uitgevoerd')
connection.disconnect()
}
```

NOTE: De waarde van de variabele "command" dient aangepast te worden naar het gewenste configuratie commando

[Scripts](https://github.com/JorenHen/Devasc_Skills_JH/tree/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Taak3) getest via DEVASC VM.


<br></br>


## Task 4: Create an challenging excited script as a network

- DEVASCVM
- CSR1000v VM
- Visual Studio Code

### Taak voorbereiding en implementatie

1. Importeer de `requests` en `json` bibliotheken om HTTP-verzoeken te verzenden en JSON-gegevens te verwerken.
2. Definieer de functie `get_device_interfaces` om de interfaces van het IOS-XE-apparaat op te halen via de RESTCONF-API.
3. Definieer de functie configure_interface om een specifieke interface van het IOS-XE-apparaat te configureren via de RESTCONF-API.
4. Voer een voorbeeldgebruik uit waarin eerst de interfaces van het apparaat worden opgehaald en vervolgens een interface wordt geconfigureerd.
5. Het voorbeeldgebruik gebruikt de opgegeven IP, gebruikersnaam en wachtwoord om verbinding te maken met het IOS-XE-apparaat en de benodigde acties uit te voeren.
6. Het script bevat foutafhandeling om mogelijke fouten tijdens de HTTP-verzoeken af te vangen en weer te geven.

### Taak troubleshooting

Het script wou eerst niet werken. Hiervoor heb ik de RESTCONF API moeten enabelen.

Moest het script alsnog niet werken voor u probeer dan:

1. De connectiviteit te controlleren: Verifieer of het apparaat toegankelijk is en er geen netwerkproblemen zijn.
2. De response status te controlleren: Controleer de HTTP-statuscodes om te zien of de verzoeken met succes zijn voltooid.

### Taak verificatie

Script uitgevoert en eventuele foutmeldingen gecontrolleerd en opgelost.

[Script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%206%20-%20Python%20network%20automation%20with%20netmiko/Taak4/Script.py)


<br></br>


# LAB 7 – YANG, NETCONFIG and RESTCONFIG

## Part 1: Install the CSR1000v VM

- DEVASCVM
- CSR1000v ISO
- VMWARE Workstation

### Taak voorbereiding en implementatie

1. VM Downloaden van leerkracht zijn one drive
2. VM Opstarten
3. Wachten tot de VM vraagt voor de ISO te installeren
4. VM afsluiten
5. DVD drive drive 1 uitwerpen
6. ISO in DVD drive 1 steken
7. VM opstarten
8. Wachten tot installatie process gedaan is

### Taak Troubleshooting

VM wou niet installeren en gaf een foutmelding:

- ISO bestand is nodig om de VM volledig te kunnen installeren. Deze was eerst niet meegegeven

- Tijdens het installatie process op niets drukken. Als de VM een keuze tussen 2 opties geeft gewoon wachten tot hij uit zichzelf verder gaat.

### Taak verifieren

[VM is geinstalleerd](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/VM%20Installatie%20success.png)

[GUI van de VM werkt](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/GUI.png)


<br></br>


## Part 2: Explore YANG Models

- DEVASCVM
- CSR100v VM
- YANG

### Taak voorbereiding en implementatie

1. DEVASCVM opstarten
2. Nieuwe directory aanmaken `mkdir pyang`
3. YANG installeren `wget https://raw.githubusercontent.com/YangModels/yang/main/vendor/cisco/xe/1693/ietf-interfaces.yang`

### Taak Troubleshooting

Geen problemen gehad tijdens deze taak. Moest u wel problemen hebben probeer dan een van de volgende opties:

- `sudo apt update` `sudo apt upgrade`
- `sudo reboot now`

### Taak verifieren

[pyang installatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/pyang%20install.png)

`pyang -v`

[pyang version](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/pyang%20version.png)


<br></br>


## Part 3: Use NETCONF to Access an IOS XE Device

- DEVASCVM
- CSR1000v VM
- Visual Studio Code

### Taak voorbereiding en implementatie

1. DEVASCVM opstarten
2. CSR1000v VM opstarten
3. SSH connctie maken naar CSR1000v VM via DEVASCVM `ssh cisco@192.168.253.128`
4. `exit`
5. Open NETCONFIG via SSH naar de CSR1000v VM `ssh cisco@192.168.253.128 -p 830 -s netconf`
6. XML code doorsturen naar de switch via de SSH code
7. Script maken om een connectie te maken via ncclient

### Taak Troubleshooting

Als NETCONFIG niet runt op de CSR1000v `config t` `netconf-yang`

### Taak verifieren

[Uitvoeren van XML code via een SSH sessie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/XML%20code%20.png)

[Directory aanmaken voor het script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/Directory%20voor%20het%20script.png)

[Script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/ncclient-netconf.py)

[Script uitvoer](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/Script%20uitvoer.png)




<br></br>


## Part 4: Use RESTCONF to Access an IOS XE Device

- DEVASCVM
- CSR1000v VM
- Vsual Studio Code

### Taak voorbereiding en implementatie

1. DEVASCVM aanzetten
2. CSR1000v VM opstarten
3. RESTCONF aanzetten op switch `conf t` `restconf`
4. `ip http secure-server`
5. `ip http authentication local`
6. Script maken en uitvoeren

### Taak Troubleshooting

Geen problemen gehad tijdens deze taak. Moest u wel problemen hebben probeer dan een van de volgende opties:

- `sudo apt update` `sudo apt upgrade`
- `sudo reboot now`

### Taak verifieren

[Restconf aanzetten](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/RESTCONF%20aanzetten.png)

[http aanzetten](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/http%20enable.png)

[Script](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%207%20-%20NETCONFIG%20and%20YANG/postmanscript.py)
