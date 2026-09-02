import requests
import pandas as pd

def fetch_pappbecher_potenzial(stadt_name="Hamburg"):
    # Overpass API Query für Gastro, Bäckereien und Tankstellen
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    area[name="{stadt_name}"]->.searchArea;
    (
      node["amenity"="cafe"](area.searchArea);
      node["amenity"="fast_food"](area.searchArea);
      node["shop"="bakery"](area.searchArea);
      node["amenity"="fuel"](area.searchArea);
    );
    out center;
    """
    
    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()
    
    locations = []
    for item in data.get('elements', []):
        lat = item.get('lat')
        lon = item.get('lon')
        tags = item.get('tags', {})
        name = tags.get('name', 'Unbenannt')
        kategorie = tags.get('amenity', tags.get('shop', 'Gastro'))
        
        # Schätzung des Becherpotenzials pro Monat basierend auf Kategorie
        potenzial_faktor = {
            'cafe': 3000,
            'fast_food': 5000,
            'bakery': 4000,
            'fuel': 2500
        }.get(kategorie, 2000)
        
        locations.append({
            'Name': name,
            'Kategorie': kategorie,
            'Lat': lat,
            'Lon': lon,
            'Geschätzter_Becherbedarf_Monat': potenzial_faktor
        })
        
    df = pd.DataFrame(locations)
    return df

# Beispielaufruf
if __name__ == "__main__":
    df_potenzial = fetch_pappbecher_potenzial("Hamburg")
    print(f"Gefundene Hotspots: {len(df_potenzial)}")
    print(df_potenzial.head())







