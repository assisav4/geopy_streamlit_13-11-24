import streamlit as st
from streamlit_folium import st_folium
import folium
from streamlit.components.v1 import html
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderInsufficientPrivileges


def get_location_by_address(address):

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
        st.info("Acesso negado: verifique o user-agent e a frequência das requisições.")
        return None
    
def map_location(lat, lon):
    """Exibe um mapa com uma marcação para a latitude e longitude fornecidas usando folium."""
    m = folium.Map(location=[lat, lon], zoom_start=16)
    folium.Marker([lat, lon]).add_to(m)
    # Renderiza o mapa no Folium e depois exibe no Streamlit
    map_html = m._repr_html_()
    html(map_html, width=700, height=500)


st.title("Conversão de endereço para Latitute e Longitude aproximada")

endereco = st.text_input('Endereço completo:')

if st.button('Localizar'):
    # A função é chamada com o texto inserido pelo usuário quando o botão é clicado.
    location = get_location_by_address(endereco)

    if location:
        #st.info(f"Latitude: {location[0]}, Longitude: {location[1]}")
        st.divider()
        map_location(*location)
    else:
        st.info("Localização não encontrada.")


