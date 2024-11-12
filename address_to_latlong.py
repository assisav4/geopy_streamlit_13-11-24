from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderInsufficientPrivileges

def get_location_by_address(address):
    """Função para converter um endereço em latitude e longitude."""
    geolocator = Nominatim(user_agent="gmcalixto@gmail.com")
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        return None
    except GeocoderInsufficientPrivileges:
        print("Acesso negado: verifique o user-agent e a frequência das requisições.")
        return None

# Exemplo de uso da função
#address = "221B Baker Street, London"
address = "Rua Visconde do Uruguai, 311, São Paulo, Brazil"
location = get_location_by_address(address)

if location:
    print(f"Latitude: {location[0]}, Longitude: {location[1]}")
else:
    print("Localização não encontrada.")
