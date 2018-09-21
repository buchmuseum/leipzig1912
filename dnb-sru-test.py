import pandas as pd
import numpy as np

from urllib.request import urlopen as uReq
import urllib
from bs4 import BeautifulSoup as soup

#Konfiguration der SRU-Suchanfrage
#mögliche record schemas: MARC21-xml, RDFxml
#BBG=Tb* Körperschaften
sru_parameter = {'version':'1.1', 'operation':'searchRetrieve', 'accessToken':'8090beb04b8a8ce79c2da2c1ee6890b8', 'query':'KOE=oelsner AND BBG=Tb* AND Leipzig', 'recordSchema':'RDFxml'}
#/sru/dnb sucht im Hauptbestand /sru/authorities sucht in der GND, Satzart wird in query festgelegt
base_url = ('https://services.dnb.de/sru/authorities?')

parameter = urllib.parse.urlencode(sru_parameter)
#Die Parameter werden an die Base-URL angehängt
retrieve_url = base_url + parameter

#Die Such-URL wird an den Webserver der DNB geschickt, das Ergebnis wird in die Variable suche_xml gepackt und die Verbindung wird wieder geschlossen
sru_raw = uReq(retrieve_url)
suche_xml = sru_raw.read()
sru_raw.close()

#Mit dem XML-Parser von BeautifulSoup wird das Ergebnis der Suche geparst.
xml_soup = soup(suche_xml, "xml")

records = xml_soup.findAll("record")

#print(records)
#print(len(records))

gnd_id = xml_soup.record.recordData.RDF.Description.gndIdentifier.contents

print(gnd_id)