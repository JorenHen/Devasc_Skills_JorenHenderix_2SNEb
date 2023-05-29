## ! Disclaimer: allen screenshots zijn in de READme gezet aan de hand van linken en geen copy paste!

# LAB 1 - Python experiments

## 1.1 Install different tools/packages on Ubuntu DEVASC-LABVM
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

Door het uitvoeren van `udo apt update && sudo apt upgrade` voorkomen we errors bij het installeren van applicaties.

### Taak verifieren 

[Installed verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%201.png)

[Jupyter werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%202.png)

[IDLE werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%203.png)


<br></br>


## 1.2 Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (1.1)

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


## 1.3 Install different tools/packages on Windows OS (deep dive exercise) ++

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

-Open Jupyter Notebook met dit commando: `python -m notebook`

### Taak verifieren

[Installed verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%205.png)

[IDLE install verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%206.png)

[IDLE werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%207.png)

[Jupyter werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%208.png)


<br></br>


## 1.4 Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++

- Python 3.8 and PIP
- Visual Studio Code
- Jupyter Notebook
- Python IDLE

### Taak voorbereiding en implementatie

- Installeer Ubuntu 22.04.1 ISO via: https://old-releases.ubuntu.com/releases/22.04.1/
- Installeer de VM
- 
1. Update en upgrade apt om errors te voorkomen `sudo apt update` `sudo apt upgrade`
2. installeer Snap voor visual studio code `sudo apt install snapd` 
- Installeer Visiual Studio Code `Sudo snap install --classic code`
3. installeer Python en pip `sudo apt intall python3` `sudo apt install python3-pip`
4. Installeer jupyter `sudo apt install jupyter`
5. installeer IDLE `sudo apt install idle`

### Taak troubleshooting

### Taak verifieren

[Install verificaties](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%209.png)

[Jupyter werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%2010.png)

[IDLE werkend verificatie](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%201%20-%20Python%20Experiments/LAB%201%20-%20Task%20Verification%2011.png)


<br></br>


# LAB 2 - Explore Rest APIs With API Simulator And Postman.

## Part 1: Explore API Documentation Using the API Simulator

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

1. Surfen naar library.demo.local
2. Naar de "Our Books" tab gaan
3. Op de knop `Click here for API docs` drukken
4. Ga dan naar POST\LoginViaBasic
5. Daarna "Try it out"
6. Op de knop `Execute` drukken

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
[Key](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/POST%20GUI%20uitvoer.png)

API Call cia [Curl](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/Curl%20succes.png)

API call [DELETE met curl](https://github.com/JorenHen/Devasc_Skills_JH/blob/master/Lab%202%20-%20Explore%20rest%20APIs%20with%20API-simulator%20and%20postman/Task%201/CURL%20delete%20met%20API%20key.png)




