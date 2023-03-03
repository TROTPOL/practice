from weather import City, Weather
import error


def get_city():
       city = input("Введіть назву міста для якого хочете отримати погоду:")
       

       if not city:
              city = 'Kyiv'
       elif city.isdigit():
              raise error.NameError()
       else:
              City.get_coords(city)
  
get_city()



