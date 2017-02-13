# -*- coding: utf-8 -*-

import codecs
import os
from xml.etree import ElementTree as etree

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROJECT_FILES_PATH = os.path.join(PROJECT_PATH, 'files')

# class GPTrackParser:

# def __init__(self, files_path, filename):
_gpxNamespace = "{http://www.topografix.com/GPX/1/1}"
_gpxTrackPointNamespace = "{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}"
_filename = '14km_activity_1568097651.gpx'

# def load(self):
file = codecs.open(os.path.join(PROJECT_FILES_PATH, _filename), mode='rb', encoding='utf-8')
tree = etree.parse(file)
# tree = tree.iterparse(file, ['end'])

# {http://www.topografix.com/GPX/1/1}trkpt text=
# {http: // www.topografix.com / GPX / 1 / 1}ele # text = 1119.199951171875
# {http: // www.topografix.com / GPX / 1 / 1}time # text = 2017 - 02 - 11 # T11: 25:36.000 # Z
# {http: // www.garmin.com / xmlschemas / TrackPointExtension / v1}hr # text = 165
# {http: // www.topografix.com / GPX / 1 / 1}extensions # text =

for elem in tree.getroot().findall("{0}{1}".format(_gpxNamespace, 'trk')):
    print(elem.tag, 'text=', elem.text)
    for elem1 in elem.findall('{http://www.topografix.com/GPX/1/1}trkseg'):
        print(elem1.tag, 'text=', elem1.text)
        ind = 0
        for elem2 in elem1.findall('{http://www.topografix.com/GPX/1/1}trkpt'):
            ind = ind + 1
            lat = elem2.get('lat')
            lon = elem2.get('lon')
            time = elem2.find('{http://www.topografix.com/GPX/1/1}time')
            ele = elem2.find('{http://www.topografix.com/GPX/1/1}ele')
            for elem3 in elem2.findall('{http://www.topografix.com/GPX/1/1}extensions'):
                for elem4 in elem3.findall('{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}TrackPointExtension'):
                    hr = elem4.find('{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr')
                print("{0} {1} {2} {3} {4}".format(ind, lat, lon, time.text, hr.text))
