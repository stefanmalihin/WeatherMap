from folium import Map, Popup
from geo import Geopoint

# Get latitude and longitude values
locations = [[31.95, 35.92], [30.43, 31.26], [32.08, 34.80]]

# Folium Map instance
mymap = Map(location=[32.08, 34.80])

for lat, lon in locations:
    # Create Geopoint instance
    geopoint = Geopoint(latitude=lat, longitude=lon)
    forecast = geopoint.get_weather()
    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round((forecast[0][1]-32)*5/9)}°C <img src="http://openweathermap.org/img/wn/{forecast[0][3]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8:-6]}h: {round((forecast[1][1]-32)*5/9)}°C <img src="http://openweathermap.org/img/wn/{forecast[1][3]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8:-6]}h: {round((forecast[2][1]-32)*5/9)}°C <img src="http://openweathermap.org/img/wn/{forecast[2][3]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8:-6]}h: {round((forecast[3][1]-32)*5/9)}°C <img src="http://openweathermap.org/img/wn/{forecast[3][3]}@2x.png" width=35>
    """
    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)
    
# Save the Map instance into HTML file
mymap.save("map.html")
