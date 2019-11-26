#shows weather of current city, location based on internet provider coordinates
import geocoder, webbrowser
g = geocoder.ip('me')
webbrowser.open('https://www.theweathernetwork.com/ca/weather/' +g.state+'/'+ g.city)

# refrences https://geocoder.readthedocs.io/api.html -> how to use geo code
# installing third-Party modules sudo pip3 install ModuleName
