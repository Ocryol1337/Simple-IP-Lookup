import requests
import sys

ipaddr = input("Insert the IP you want to get information about - ")
r = requests.get(f"https://ipapi.co/{ipaddr}/json")
geo = r.json()
if ipaddr == "":
 sys.exit("You did not add an IP to lookup!")
else:
  print(f"IP - {geo['ip']}")
print(f"IP Type - {geo['version']}")
print(f"City - {geo['city']}")
print(f"Country - {geo['country_name']}")
print(f"Country Code - {geo['country_code']}")
print(f"In Europe - {geo['in_eu']}")
print(f"Postal - {geo['postal']}")
print(f"Continent Code - {geo['continent_code']}")
print(f"Country TLD (Top-level domain) - {geo['country_tld']}")
print(f"Latitute - {geo['latitude']}")
print(f"Longitude - {geo['longitude']}")
print(f"Currency - {geo['org']}")
print(f"Population - {geo['country_population']}")
print(f"Region - {geo['region']}")
print(f"Google Maps Link - https://www.google.com/maps?q={geo['latitude']},{geo['longitude']}")
