# GeoBIM & Supply Chain Hotspot Analyzer

Eine Open-Source Data-Pipeline zur Analyse und 3D-Visualisierung von B2B-Absatzpotenzialen (Verpackungs- / Pappbecherlogistik) an bundesweiten Infrastruktur- und Gastronomie-Knotenpunkten.

## 🏗️ Architektur & Tech-Stack

Das Projekt verknüpft Geoinformationssysteme (GIS), OpenBIM-Standards und B2B-Logistikprozesse:

* **Data Engine (Python):** Automatisierter Abruf von Point-of-Interest-Daten (Gastro, Tankstellen, Bäckereien, Bahnhöfe) über OpenStreetMap / Overpass API.
* **Backend & Business-Logik (Java / Spring Boot):** Verwaltung von Großhändlern, Lagerbeständen, Import-Margen aus der Türkei und Distributionswegen.
* **GIS & Spatial DB (QGIS / PostGIS):** Räumliche Netzwerkanalysen, Isochronen-Berechnungen und Frequenz-Scoring.
* **3D-BIM Visualization (Speckle / IFC):** Aggregation von Gebäude- und Infrastrukturdaten zur 3D-Hotspot-Darstellung im Webbrowser.

## 🚀 Quickstart (Python Script)

```bash
# Repository klonen
git clone [https://github.com/AEnsar/geobim-pappbecher-analyzer.git](https://github.com/AEnsar/geobim-pappbecher-analyzer.git)
cd geobim-pappbecher-analyzer

# Abhängigkeiten installieren
pip install pandas requests

# Skript ausführen
python main.py

