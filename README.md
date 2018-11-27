# Leipzig 1912
Eine Datenbank Leipziger Unternehmen des Buchgewerbes 1912. Die Daten wurden dem Leipziger Adressbuch 1913 entnommen und repräsentieren damit den Stand der Dinge des Vorjahres 1912. Die Datenbank enthält Namen, historische Flurstück- und Brandkatasternummern, historische Adressen sowie deren Entsprechungen des Jahres 2018, sofern es die Adressen noch gibt.

## Feldbeschreibung der csv-Datenquelle
Id - Eineindeutige Id eines jeden Datensatzes, bitte nicht verändern.

FirmenNr - Jede Firma hat eine Nummer, Firmen können doppelt vorkommen, weil sie mehrere Standorte hatten

HaeuserNr - zur eindeutigen Identifizierung der Gebäude

ETRS_UTM33N_X

ETRS_UTM33N_Y

Firma - bereinigter Name der Firma

Vorlage - Name der Firma, wie er im historischen Adressbuch stand

FlurstuecksNr - historische Flurstücksnummer

BrandkatasterNr - historische Brandkatasternummer

Hausname - manche Häuser hatten Eigennamen

HausNr - historische Hausnummer in der Adressangabe

Strasse - historische Straßenadresse

Strassenteil

Stadtteil - historische Stadtteilbezeichnung

Gewerbename - Eigenbezeichnung der Firma

Gewerbetyp - Zuordnung zu einem Gewerbetyp

STR_NAME_2018 - Straßenname 2018

HNR_2018 - Hausnummer 2018

PLZ_2018 - Postleitzahl 2018

FLURSTUECKSNR_2018 - Flurstücksnummer 2018

SBZ_NR_2018 - Stadtbezirk-Nr. 2018

SBZ_NAME_2018 - Stadtbezirk Name 2018

OT_NR_2018 Ortsteilnummer 2018

OT_NAME_2018 Ortsteilname 2018

## Beschreibung der Skripte

### parse-data.py

Das Skript rechnet die ETRS_UTM33N-Koordinaten in WGS84-Koordinaten um und gibt eine geojson-Datei aus. Es kann ausgewählt werden, welche Spalten der csv in die geojson-Daten übernommen werden sollen.

### gnd-lookup.py

Über die SRU-Schnittstelle der Deutschen Nationalbibliothek wird in den Normdaten der Gemeinsamen Normdatei nach Datensätzen zu den einzelnen Unternehmen gesucht. Mögliche Treffer der Suchanfrage werden in gnd.csv gespeichert. Die Daten müssen in einem nächsten Schritt validiert werden.

### leaflet-map.html

Hier werden die Geojson-Daten mit Leaflet auf einer Karte dargestellt. Work in Progress.

## Credits

Die Daten wurden in den 1990er-Jahren im Deutschen Buch- und Schriftmuseum der Deutschen Nationalbibliothek aus dem historischen Adressbuch der Stadt Leipzig (http://d-nb.info/013304410) in eine Access-Datenbank übertragen. Die Geokoordinaten sowie die modernen Adressdaten wurden 2018 vom  Amt für Geoinformation und Bodenordnung, Abteilung Digitale Kartographie der Stadt Leipzig ergänzt.
