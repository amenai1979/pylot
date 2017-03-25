__author__ = 'Alexandre Menai amenai@amenai.net'
'''
The weather module intends to grab pilot weather from the aviation weather services in the USA
'''
#TODO put the following global parameters into a configuration file later on
WEAHTER_HOSTNAME="aviationweather.gov"
METAR_PATH="/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString="
#end global parameters
import httplib
import utilities.XML2Py as XML2Py
class Weather:

    def __init__(self, start_date=1490468686,duration=86400,departure_airfield='KBED',destination_airfield='KRKD'):
        """
        initializes a weather object.
        :param start_date: the start date in epoch
        :param duration: the duration of the flight in seconds
        :param departure_airfield: is the 4 letter ICAO identifer of the departure airfield
        :param destination_airfield: is the 4 letter ICAO identifer of the destination airfield
        :return: the handle for the Object.
        """
        self.start_date=start_date
        self.duration=duration
        self.departure_airfield=departure_airfield
        self.destination_airfield=destination_airfield

    def grab_airfield_weather(self, airfield='KBED', hours_before_now=1):
        #construct the path and params
        requestPath=METAR_PATH+airfield+"&hoursBeforeNow="+str(hours_before_now)
        #initiate the connection
        connection=httplib.HTTPConnection(WEAHTER_HOSTNAME)
        # Get the METAR
        connection.request('GET',requestPath)
        metar_xml=connection.getresponse().read()
        #close the connection
        connection.close()
        deserialized_metar = XML2Py.XML2Py().parse(metar_xml)
        return deserialized_metar
        #TODO scale down the useless information
