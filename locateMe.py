#opens current city on google map
import geocoder, webbrowser
g = geocoder.ip('me')
webbrowser.open('https://www.google.com/maps/place/' + g.city)

# refrences https://geocoder.readthedocs.io/api.html -> how to use geo code
# installing third-Party modules sudo pip3 install ModuleName
