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