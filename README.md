# tube_transkripter

# Kleines Helfertool

Dies ist ein kleines Helfertool, erstellt mit Hilfe eines Large Language Models (LLM). Ich habe es benutzt, um zu sehen, was man mit nur Prompt-Eingaben erstellen kann.

## 💡 Motivation & Reflexionen

Dieses Projekt entstand aus der Neugier, zu erkunden, was sich mit reinen LLM-Prompts erstellen lässt. Einige Gedanken dazu:

- **Alles ist LLM-generiert** – Der Code und die Dokumentation wurden mithilfe von KI erstellt. Ob es "abgeschrieben" ist? Keine Ahnung. 😅
- **Detailgrad der Umsetzung** – Die Idee musste extrem detailliert beschrieben werden (fast wie Programmieren). Warum dann nicht gleich selbst codieren? Nun, Zeitersparnis! ⏳
- **Zeitersparnis** – Dank LLM musste ich mich nicht tief in PyQt einarbeiten – und es sieht trotzdem gut aus. 🎨
- **Bugs & Optimierung** – Fehlerbehebung und Verbesserungen liegen beim Nutzer. Ist es den Aufwand wert? Für mich nicht, aber das entscheidet jeder selbst. 🐞
- **Nützlichkeit** – Ob das Tool sinnvoll ist? Kommt darauf an, was man braucht. 🤷

## ⚠️ Bekannte Einschränkungen

    Unterstützt nur YouTube-Links mit vorhandenem Transkript.

    Die UI ist grundlegend gehalten und nicht responsiv.

## 📄 Lizenz

MIT-Lizenz – Nutzung und Modifikation erwünscht!

## 📋 Beschreibung
Dieses Tool ermöglicht das gleichzeitige Extrahieren von Transkripten aus bis zu fünf YouTube-Videos. Die gesammelten Transkripte können als Textdatei gespeichert und anschließend mit einem LLM (z. B. ChatGPT) weiterverarbeitet werden, um strukturierte Zusammenfassungen zu erstellen.

## 🚀 Features
- Extrahiert Transkripte aus YouTube-Links (bis zu 5 gleichzeitig).
- Speichert Transkripte als `.txt`-Datei.
- Integrierte Hilfefunktion mit Anleitung zur LLM-Nachbearbeitung.

## Installation

Um dieses Tool zu verwenden, klonen Sie das Repository und installieren Sie die benötigten Abhängigkeiten:

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt

## Screenshot

