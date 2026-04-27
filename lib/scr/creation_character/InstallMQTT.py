import utime
import network
import mip

#########################################################################
# MQTT installeres på Pico via WiFi/Internet.
# Vi skal derfor først oprette forbindelse via WiFi.
#########################################################################
#########################################################################
# Opgave 1:
# Udfyld funktionen herunder (TODO), så den laver en forbindelse til ITEK x WiFi
# - Brug ITEK ssid og password
# - Vent på WiFi forbindelse OK (brug wlan.status() )
#     - Hvis OK -> Udskriv IP adresse
#     - Returner wlan object
#########################################################################
def connectWiFi():
    print('Connecting to WiFi...')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # TODO
    wlan.connect("ITEK 2nd", "2nd_Semester_E25")

    # Vent på WiFi forbindelse:
    print("Waiting for connection...")
    timeout = 10
    while timeout > 0 and wlan.status() == network.STAT_CONNECTING:
        print(f"Connecting...")
        utime.sleep(1)
        timeout -= 1
    # TODO:
    # Læs wlan status indtil der er oprettet forbindelse. Eller afslut hvis der går mere end 10 sekunder uden forbindelse
    # Hint: wlan status returneres som "network.STAT_xxx"
    # Se https://docs.micropython.org/en/latest/library/network.WLAN.html
    ...

    # TODO:
    # Udskriv IP adresse hvis status er OK, eller udskriv fejltekst hvis den fejlede:
    if wlan.isconnected():
        print("Connection successful")
        print("IP adresse:", wlan.ifconfig()[0])
    else:
        print("WiFi forbindelse fejlede!")

    # Returner wlan object
    return wlan

#########################################################################
# Opgave 2: Installer MQTT package på Pico.
# Her bruger vi "mip install" som kan installere direkte fra
# micropython-lib, GitHub mm.
#########################################################################
# Kald funktionen som opretter WiFi forbindelse:
wlan = connectWiFi()

# Hvis forbindelse OK, installer MQTT package:
if wlan.isconnected():
    # TODO: Installer pakken "umqtt.simple" med "mip install". Se https://docs.micropython.org/en/latest/reference/packages.html
    print("Installing MQTT package...")
    try:
        mip.install("umqtt.simple")
        print("Installation successful!")
    except Exception as e:
        print(f"Installation failed: {e}")

    # Luk WiFi efter installation
    wlan.active(False)
    wlan.deinit()