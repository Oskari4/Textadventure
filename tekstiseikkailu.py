import time

hahmon_nimi = ""

def kysy_hahmon_nimi():
    global hahmon_nimi
    hahmon_nimi = input("Kerro hahmosi nimi: ")
    
def aloitus():
    kysy_hahmon_nimi()
    print(f"Tervetuloa seikkailuun {hahmon_nimi}!")
    
def askel1():
    print("Olet pimeällä kujalla. Saavut risteykselle kujalla.")
    valinta = input("Kumpaan suuntaan jatkat? (vasen/oikea): ")
    if valinta.lower() == "vasen":
        print("Saavuit autiolle talolle.")
        time.sleep(2)
        askel2()
    elif valinta.lower() == "oikea":
        askel3()
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        askel1()
        
def askel2():
    print("Astuit sisään autioon taloon.")
    time.sleep(2)
    print("Kuulet askelia yläkerrasta.")
    time.sleep(2)
    print("Mitä haluat tehdä?")
    time.sleep(2)
    print("1. Nouse rappusia ylös.")
    print("2. Poistu talosta.")
    valinta = input("Valitse toiminta (1/2): ")
    if valinta == "1":
        print("Aloit varovasti nousemaan rappuja ylös. Kesken matkan raput romahtavat. Peli Päättyi.")
    if valinta == "2":
        print("Poistuit talosta ja menit takaisin toiseen suuntaan")
        time.sleep(2)
        askel3()

def askel3():
    print("Jatkat matkaasi kujalla.")
    time.sleep(2)
    print("Eteesi ilmestyy joki, näet pienen matkan päässä romahtaneen sillan.")
    time.sleep(2)
    print("Mitä haluat tehdä?")
    time.sleep(2)
    print("1. Yritä uida joen yli.")
    print("2. Koita ylittää joki romahtaneen sillan kautta.")
    print("3. Jatka matkaa joen vartta pitkin")
    valinta = input("Valitse toiminta (1/2/3): ")
    if valinta == "1":
        print("Mestari uimarina yritit uida joen yli, mutta virtaus oli liian kova ja sinä hukuit. Peli päättyi.") 
    elif valinta == "2":
        print("Menit sillan luo, mestari akrobaattina hyppelit kuin pieni balleriina romahtaneilla sillan palasilla. Pääsit turvallisesti joen yli.")   
        time.sleep(2)
        askel4()
    elif valinta == "3":
        print("Jatkoit matkaa joen vartta pitkin. Hetken kuluttua karhu ilmestyi puskasta ja raateli sinut. Peli päättyi.")
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        askel3()
    
def askel4():
    print("Jatkat matkaa päästyäsi joen yli.")
    time.sleep(2)
    print("Hetken kuluttua näet hahmon makaamassa tiellä.")
    time.sleep(2)
    print("Mitä haluat tehdä?")
    time.sleep(2)
    print("1. Tutki hahmoa.")
    print("2. Jatka matkaa.")
    valinta = input("Valitse toiminta (1/2): ")
    if valinta == "1":
        print("Päästyäsi lähemmäksi tunsit kumahduksen takaraivossasi. Tulit rosvojoukon väijytyksi ja kuolit. Peli päättyi.")   
    elif valinta == "2":
        print("Päätit jättää hahmon huomiotta ja jatkoit matkaa.")
        time.sleep(2)
        askel5()
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        askel4()  
        
def askel5():
    print("Hetken kuluttua saavuit kotiasi.")
    time.sleep(2)
    print("Mitä haluat tehdä?")
    time.sleep(2)
    print("1. Mene pesulle.")
    print("2. Mene jääkaapille.")
    valinta = input("Valitse toiminta (1/2): ")
    if valinta == "1":
        print("Menit kylpyhuoneeseesi. Nousit suihkuun mutta liukastuit ja mursit kallosi. Peli päättyi.")
    if valinta == "2":
        print("Menit jääkaapille.")   
        time.sleep(2)
        print("Siellä sinua odottaa yksi iso olut.")
        time.sleep(2)
        print(f"Sinulla {hahmon_nimi}, on ollut pitkä päivä. Korkkaat oluen ja menet katsomaan lempi TV ohjelmaasi.")
        time.sleep(2)
        print("Onneksi olkoon, voitit pelin!")
        
def main():
    aloitus()
    askel1()
    
if __name__ == "__main__":
    main()
    