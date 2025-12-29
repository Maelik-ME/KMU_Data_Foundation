# KMU Data Foundation

Eine einfache, nachvollziehbare Projektstruktur für sauberes Datenmanagement
in kleinen und mittleren Unternehmen (KMU).

## Zweck

Dieses Repository zeigt eine praxiserprobte Arbeitsweise,
wie Unternehmensdaten strukturiert, gespeichert und verarbeitet werden können –
ohne unnötige Komplexität oder schwer wartbare Systeme.

Der Fokus liegt auf:
- klarer Datenstruktur
- nachvollziehbaren Verarbeitungsschritten
- robuster, wartbarer Umsetzung

## Typische Probleme in KMUs

Viele KMUs arbeiten mit:
- verstreuten Excel-Dateien
- manuellen Reports
- fehlender Datenhistorie
- unklarer Datenherkunft
- schwer nachvollziehbaren Berechnungen

Dieses Projekt adressiert diese Probleme durch einfache,
klare und überprüfbare Datenstrukturen.

## Projektstruktur

- `data/raw`  
  Unveränderte Originaldaten (niemals bearbeiten)

- `data/processed`  
  Bereinigte und strukturierte Daten

- `data/output`  
  Daten für Reports, Exporte oder Weitergabe

- `src`  
  Wiederverwendbare Funktionen für Datenverarbeitung

- `metadata`  
  Beschreibungen der Datensätze  
  (Struktur, Herkunft, Bedeutung, Annahmen)

- `notebooks`  
  Exploration und fachliche Nachvollziehbarkeit

## Dataset-Konfiguration

Der verwendete Datensatz wird zentral in `src/config.py` definiert.

Dadurch kann dieselbe Pipeline-Struktur
für unterschiedliche Datensätze wiederverwendet werden,
ohne die Pipeline-Logik anzupassen.

## Annahmen & Grenzen

Diese Pipeline geht davon aus:
- CSV-Dateien werden vom Fachbereich bereitgestellt
- Es existiert genau ein Primärschlüssel (`orderid`)
- Datenqualitätsprobleme werden nicht automatisch korrigiert

Die Pipeline stoppt, wenn:
- doppelte Primärschlüssel erkannt werden
- (optional) fehlende Werte gemäß Konfiguration nicht erlaubt sind

Die Pipeline:
- dedupliziert keine Daten automatisch
- schätzt keine fehlenden Werte
- verändert keine Geschäftslogik ohne explizite Konfiguration

## Bewusste Entscheidungen

Dieses Projekt verzichtet bewusst auf:
- Machine Learning
- komplexe Cloud-Architekturen
- Framework-Overhead

Ziel ist eine Lösung, die verstanden,
überprüft und langfristig gewartet werden kann.

## Zielgruppe

Dieses Projekt richtet sich an:
- kleine und mittlere Unternehmen
- Verantwortliche für Finanzen, Operations oder IT
  (CFO, COO, IT-Leitung)
- Organisationen mit Fokus auf Stabilität und Nachvollziehbarkeit

## Betrieb & Nutzung

### Voraussetzungen
- Windows
- Anaconda oder Miniconda
- Conda Environment: `zyklop`

### Pipeline ausführen

**Über Kommandozeile:**
```bash
python -m src.pipeline
