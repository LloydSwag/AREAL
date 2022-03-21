import os

def clear():
    os.system('cls')

# Funskjon for å skrive hovedmenyen til skjerm
def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Beregn areal for kvadrat")
    print("2. Beregn areal for rektangel")
    print("3. Beregn areal for trekant")
    print("4. Beregn areal for parallellogram")
    print("5. Beregn areal for rombe")
    print("6. Beregn areal for trapes")
    print("7. Beregn areal for sirkel")
    print("8. Avslutt")


# Funksjon for å beregne arealet av et kvadrat skrives her. Funsjonen skal ta imot et parameter (s)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def kvadratareal(s):
    kvadratareal_regning = s * s
    return(kvadratareal_regning)

    

# Funksjon for å beregne arealet av et rektangel skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def rektangelareal():
    g_input = float(input("Oppgi lengde på kvadrat: "))
    h_input = float(input("Oppgi høyde på kvadrat: "))

    rektangelareal_regning = g_input * h_input

    print(f"Svaret er {rektangelareal_regning} cm2")

# Funksjon for å beregne arealet av en trekant skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def trekantareal():
    g_input = float(input("Oppgi lengde på trekant: "))
    h_input = float(input("Oppgi høyde på trekant: "))

    trekantareal_regning = g_input * h_input

    print(f"Svaret er {trekantareal_regning/2} cm2")

# Funksjon for å beregne arealet av et parallellogram skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 1 har ansvaret for å lage denne funksjonen
def parallellogramareal():
    g_input = float(input("Oppgi lengde på parallellogram: "))
    h_input = float(input("Oppgi høyde på parallellogram: "))

    parallellogramareal_regning = g_input * h_input

    print(f"Svaret er {parallellogramareal_regning} cm2")

# Funksjon for å beregne arealet av en rombe skrives her. Funsjonen skal ta imot to parameter (g og h)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen
def rombe_areal():
    g_input = float(input("Oppgi grunnlinjen i romben"))
    h_input = float(input("Oppgi høyden i romben"))

    rombeareal_regning =  g_input * h_input

    print(f"svaret er {rombeareal_regning}cm^2")

# Funksjon for å beregne arealet av en trapes skrives her. Funsjonen skal ta imot tre parameter (a, b og h)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen


# Funksjon for å beregne arealet av en sirkel skrives her. Funsjonen skal ta imot et parameter (r)
# Funksjonen skal returnere arealet
# Utvikler 2 har ansvaret for å lage denne funksjonen

   

# Programmet starter her
ans="Start"
while ans != "8":
    clear()
    skriv_meny()
    
    ans=input("> ") 
    if ans=="1":
        clear()
        print("\nHer bergnes arealet av et kvadrat")
        s_input = float(input("Oppgi side på kvadrat: "))
        print("Svaret er: ", kvadratareal(s_input))
        venter=input("Trykk ENTER for å fortsette!")
    elif ans=="2":
        clear()
        print("\nHer bergnes arealet av et rektangel")
        venter=input("Trykk ENTER for å fortsette!")
        rektangelareal()
        venter=input("Trykk ENTER for å fortsette!")
    elif ans=="3":
        clear()
        print("\nHer bergnes arealet av en trekant")
        venter=input("Trykk ENTER for å fortsette!")
        trekantareal()
        venter=input("Trykk ENTER for å fortsette!")
    elif ans=="4":
        clear()
        print("\nHer bergnes arealet av et parallellogram")
        venter=input("Trykk ENTER for å fortsette!")
        parallellogramareal()
        venter=input("Trykk ENTER for å fortsette!")
    elif ans=="5":
        clear()
        print("\nHer bergnes arealet av en rombe")
        venter=input("Trykk ENTER for å fortsette!") 
        rombe_areal()
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="6":
        clear()
        print("\nHer bergnes arealet av en trapes")
        venter=input("Trykk ENTER for å fortsette!")         
        #trapes
    elif ans=="7":
        clear()
        print("\nHer bergnes arealet av en sirkel")
        venter=input("Trykk ENTER for å fortsette!") 
        #sirkel
print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")