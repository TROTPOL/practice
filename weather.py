#!/usr/bin/env python3

import json
from urllib.request import urlopen
import error

TOK = b'\xff\xfe6\x00a\x002\x006\x009\x006\x00f\x006\x00d\x002\x00b\x00a\x004\x006\x005\x007\x003\x008\x00f\x00e\x001\x00e\x00b\x00f\x007\x00a\x007\x00c\x00a\x000\x00f\x008\x00'

ENDPOINT_URL = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric&lang=ua'

GEO_URL = 'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}'

class City():

	def get_coords(city):
		try:

			key = TOK.decode('utf-16')
			url = GEO_URL.format(city=city, key=key)
			data = City.make_request(url)
			lat = data[0]['lat']
			lon = data[0]['lon']
			city = data[0]['name']
			print('Місто: ', city)
			print('Координати: ', lat, lon)
			temp = Weather.request_curtemp(lat, lon)
			return (city, lat, lon)

		except IndexError:
			raise error.CityNameError()
	    

	def make_request(url):
		response = urlopen(url)
		data = response.read()
		data = data.decode('utf-8')
		res = json.loads(data)
		return res

	
class Weather(City):

	
	def request_curtemp(lat, lon):
		key = TOK.decode('utf-16')
		url = ENDPOINT_URL.format(lat=lat, lon=lon, key=key)
		resp = City.make_request(url)
		temp2 = Weather.get_temp(resp)
		print('Температура: ', temp2, '\u00b0C')
		feels = Weather.get_feels_temp(resp)
		print('Відчувається як:', feels, '\u00b0C')
		wind = Weather.get_wind(resp)
		print('Швидкість вітру:', wind, 'м/с')
		pressure = Weather.get_pressure(resp)
		print('Атмосферний тиск:', pressure, 'гПА', pressure*0.75, 'mm')
		return temp2
	    
	def get_temp(resp):
		main = resp['main']
		main_temp = float(main['temp'])
		return main_temp
	
	def get_feels_temp(feels):
		main = feels['main']
		main_feels = float(main['feels_like'])
		return main_feels
	
	def get_wind(wind):
		main = wind['wind']
		main_wind = float(main['speed'])
		return main_wind
	
	def get_pressure(pressure):
		main = pressure['main']
		main_pressure = float(main['pressure'])
		return main_pressure

if __name__ == '__main__':
	import sys
	main(sys.argv)
