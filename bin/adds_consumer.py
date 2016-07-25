__author__ = 'amenai'
from urllib2 import Request, urlopen, URLError

from xmltodict import parse


class AirfieldWeather:
    def __init__(self, airfield='KBED', deltatime='0.5'):
        """
        :param airfield: string,  the OACI Airflield identifier
        :param deltatime: string, how many hours prior to present time do you want data to be retrieved for
        :return:
        """
        self.retrieve_fields = ['altim_in_hg', 'flight_category', 'elevation_m', 'wind_speed_kt', 'wind_gust_kt',
                                'wind_dir_degrees', 'visibility_statute_mi', 'temp_c', 'dewpoint_c', 'sky_cover',
                                'observation_time']
        self.airfield = airfield
        self.baseUrl = 'http://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=' + airfield + '&hoursBeforeNow=' + deltatime + '&fields=' + (
        ','.join(self.retrieve_fields))
        request = Request(self.baseUrl)
        try:
            response = urlopen(request)
            self.metar = parse(response.read(), process_namespaces=True)
            # there could be two cases here, if there is more than one metar the return object is a list, otherwize it's a dict
            #handle the list case:
            if self.metar['response']['data']['@num_results'] == '0':
                raise URLError, "0 results"
            elif int(self.metar['response']['data']['@num_results']) > 1:
                #take the latest value which corresponds to the first item
                self.__dict__.update((self.metar['response']['data']['METAR'])[0])
            else:
                #process the dict directly
                self.__dict__.update(self.metar['response']['data']['METAR'])
                #altim_in_hg,flight_category,elevation_m,wind_speed_kt,wind_gust_kt,wind_dir_degrees,visibility_statute_mi,temp_c,dewpoint_c,sky_cover,observation_time
        except URLError, e:
            print('No metar could be retrieved, error code:', e)

    def get_elevation_feet(self):
        """
        :return: elevation of the weather statino that generated the observation in feet
        """
        if hasattr(self, 'elevation_m'):
            return str(float(self.elevation_m) * 3.28084)
        else:
            raise AttributeError, 'elevation_m not found'

    def get_visibility_feet(self):
        """
        :return: the visibility in feet
        """
        if hasattr(self, 'visibility_statute_mi'):
            return str(float(self.elevation_m) * 5280)
        else:
            raise AttributeError, 'visibility_statute_mi not found'

    def get_temp_f(self):
        """
        :return: temperature in F degrees
        """
        if hasattr(self, 'temp_c'):
            return str(32 + (float(self.temp_c) * 9 / 5))
        else:
            raise AttributeError, 'temp_c not found'

class EnrouteWeather:
    def __init__(self):
