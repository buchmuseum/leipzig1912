import pandas as pd
import numpy as np

from urllib.request import urlopen as uReq
import urllib
from bs4 import BeautifulSoup as soup


def gnd_lookup(suchterm):
    #suchterm_encode = urllib.parse.quote_plus(suchterm)

    retrieve_url = "https://services.dnb.de/sru/authorities?recordSchema=RDFxml&operation=searchRetrieve&version=1.1&maximumRecords=50&accessToken=8090beb04b8a8ce79c2da2c1ee6890b8&query=KOE%3D" + urllib.parse.quote(suchterm) + "+AND+BBG%3DTb%2A+AND+Leipzig"

    # Die Such-URL wird an den Webserver der DNB geschickt, das Ergebnis wird in die Variable suche_xml gepackt und die Verbindung wird wieder geschlossen
    sru_raw = uReq(retrieve_url)
    suche_xml = sru_raw.read()
    sru_raw.close()

    # Mit dem XML-Parser von BeautifulSoup wird das Ergebnis der Suche geparst.
    xml_soup = soup(suche_xml, "xml")

    records = xml_soup.findAll("record")
    idn = []
    for record in records:
        idn.append(record.recordData.RDF.Description.gndIdentifier.text)
    print(suchterm + str(idn))
    return str(idn)


# einlesen der csv-datei
df = pd.read_csv("Leipzig-1912-komplett-flat.csv", delimiter=";", header=0, index_col=0, usecols=['Id', 'Firma'])

df['idn'] = df.apply(lambda row: gnd_lookup(row['Firma']), axis=1)

df.to_csv('gnd.csv', sep=';')
