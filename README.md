### Leitfaden Aufgaben Bearbeiten
- Einen Branch pro Aufgabe (zB Erstelle Kapitel xy, Korrigiere alle Rechtschreibfehler in den Kapiteln)
- Naming convention branches: origin/aufgabeOderKapitel
- Folien auf Google Drive in allgemein/02_kurse/01_kursfolien/python hochladen
- Je Aufgabe eine zusätzliche Bonus-Aufgabe (außer Kap. 13)
- Code: Kapitelüberschrift im Code H1, Aufgabenüberschrift in H2
- Code: Jeweils ein Block für: kurze Erklärung vor der Aufgabe (markdown), Aufgabenstellung (markdown), Zelle für Aufgabenbearbeitung mit Lösung (pyhton)
- Code: Vor der Lösung ein `# Write your code below this line` schreiben, damit Lösungen per Script automatisch für Teilnehmende gelöscht werden können
- Folien: am Ende des Kapitels Feedback QR-Code (im Drive bei Folien ohne Lösung)
- **Bitte an den Folien und dem Notebook zu _Kapitel 9: Listen_ orientieren** 

### Next Steps & TODOs
- Aufgaben auf Deutsch übersetzen

# python-for-beginners
Weitere Dokumente: Google Drive -> Geteilte Ablage/EduRef WS23/python

## Notebooks
- ein Jupyter Notebook & Foliensatz pro Kapitel
- Notebooks bestehen aus Aufgaben-, Erklär- und Zusatzaufgabenblocks
- Erklärblocks...
  - beinhalten eine Erklärung des vorher neu eingeführten Themas in 1-2 Sätzen...
  - und ein Code-Beispiel, welches genauso in den Folien benutzt wird
  - als Markdown-Zelle
- Aufgabenblocks...
  - bestehen aus einer Aufgabe zum vorher neu eingeführten Thema
  - bestehen aus dem Namen der Aufgabe als Überschrift und der Aufgabenstellung in einer Markdown-Zelle...
  - und einer leeren/mit der Lösung versehenen Code-Zelle
  - weisen auf die Zusatzaufgabe hin
- Erklärblock- und Aufgabenblock wechseln sich ab
- Zusatzaufgabenblöcke...
  - beinhalten mindestens eine weitere Aufgabe pro im Notebook behandelter Aufgaben
  - stehen am Ende des Notebooks
- Finaler Zellblock vor Zusatzaufgaben besteht aus QR Code zu Google Form mit Umfrage zur Schwierigkeit des Kurses

## Kursinhalt
#### 1. Einführung in Python
   1. Naming conventions
   2. Indentation
#### 2. Einführung in IDEs & Jupyter Notebook
   1. Was sind IDEs?
   2. Wie funktionieren Zellen?
   3. Live Demo
      1. Wie führe ich Code aus?
      2. Wie öffne ich Code-Dateien
#### 3. `print`-Befehl + STring Konkatenation
#### 4. Datentypen + Variablen
   1. Datentypen `int, float` 
   2. `int(), float(), str()`-Methoden
#### 5. Input-Funktion
#### 6. Arithmetische Operationen
   1. Addition
   2. Subtraktion
   3. Multiplikation
   4. Division
   5. Potenzierung
#### 7. Booleans & Boolsche Operatoren
   1. Boolean als Datentyp
   2. AND
   3. OR
   4. NOT
#### 8. if-else-Anweisungen
   1. Einführung in Indentation
   2. `if()`-Anweisung
   3. `else`-Anweisung
   4. `elif()`-Anweisung
#### 9. Listen
   1. Erstellen von Listen
   2. Werte hinzufügen
   3. Werte indizieren & auslesen
   4. Werte ändern
   5. Werte löschen
#### 10. Dictionaries
   1. Erstellen von Dictionaries
   2. Werte hinzufügen
   3. Werte indizieren & auslesen
   4. Werte ändern
   5. Werte löschen 
#### 11. For-Schleifen
   1. mit Listen
   2. mit `range()`-Funktion
   3. mit `keys()` in Dictionary
   4. über String iterieren
   5. `break`, `continue`
   6. Zusatzaufgabe: Palindromchecker
#### 12. Funktionen
   1. Erinnerung an input-Funktion, Indentation
   2. Argumente
   3. `return`-Statements
#### 13. Packages oder Spiele
   1. matplotlib, pandas
   2. Hangman, Nummern raten, Tic Tac Toe, Schere Stein Papier

## Folien
- in PowerPoint
- am Anfang jedes Kapitels eine Folie mit Tipps & grober Übersicht für Personen, die Kurs halten
- Ausführliche Motivation, Erklärung & Code-Beispiele der Themen
- Code Beispiele aus Erklärblocks als Screenshots
- Am Ende des Kapitels: Hinweis auf QR Code im Notebook (bitte mit Handy scannen) & QR Code selbst

## Genutzte Software: 3xx-Laptops (Windows)
- Visual Studio Code
  - die im Kurs genutzte IDE
  - benötigt evtl weitere Extensions für die Jupyter Notebook Integration
- Jupyter Notebook
  - integriert in VSCode werden wir in Notebooks programmieren
  - für die erste Installation von Python & Jupyter Notebook benötigt
- Git for Windows
  - zum Aktualisieren der Aufgaben-Notebooks, die in GitHub liegen (per Pull-Befehl) um sie lokal auf jedem Rechner zu haben
  - Nützlich um Code zurücksetzen (nach Bearbeitung durch Teilnehmer)
- Firefox
  - von nun an standardmäßiger Browser auf allen Laptops
- MiniConda
  - für Package Management
- VSCode-Verknüpfung auf Desktop
  - heißt <i>Python-Course</i>
  - führt direkt zu den Notebooks ohne Lösungen in VSCode 

## Genutzte Software: 4xx-Laptops (Ubuntu)
- Visual Studio Code
- git
  - `sudo apt install git`
- miniconda
  - von Website per Terminal installieren
  - beinhaltet Python 3.x
- ipykernel
  - installation mit miniconda: `conda install ipykernel`
- python-for-beginners-Ordner
  - auf Desktop klonen mit `git clone https://github.com/eduref/python-for-beginners`
- VS Code Verknüpfung
  - in Seitenleiste ziehen
  - öffnet automatisch zuletzt geöffneten Ordner -> python-for-beginners/exercises vor neuem Kurs öffnen
- Jupyter Notebook
  - in VS Code mit PopUp installieren
### Installation



