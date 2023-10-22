import pandas as pd
import folium
import os 
import explorer

def draw_map(data: pd.DataFrame, folder: str, name: str) -> None:
    starting_latitude, starting_longitude = data['stop_lat'].mean(), data['stop_lon'].mean()

    map = folium.Map(location=[starting_latitude, starting_longitude], zoom_start=12)

    data = data[['route_long_name', 'stop_id', 'stop_name', 'stop_lon', 'stop_lat']]
    for row in data.iterrows():
        row_values = row[1]
        folium.Marker([row_values['stop_lat'], row_values['stop_lon']], popup=row_values['stop_name']).add_to(map)
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    map.save(f"{folder}/{name}.html")
        
data = explorer.load_data("data/arrets-lignes.csv")
filtered_data = explorer.filter_lines_by_id(data, explorer.METRO_LINES)
draw_map(filtered_data, "export", "metro")
