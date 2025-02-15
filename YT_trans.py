import sys
import re
#import time
#import csv
import markdown
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QTextEdit, QSplitter, QMessageBox, QLabel, QTextBrowser, QFileDialog
)
from PyQt5.QtCore import Qt
from youtube_transcript_api import YouTubeTranscriptApi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Transkript")
        self.setWindowState(Qt.WindowMaximized)

        # Load configuration
        #self.api_url = ""
        #self.api_key = ""
        #try:
        #    with open('conf.csv', newline='') as csvfile:
        #       reader = csv.DictReader(csvfile)
        #        for row in reader:
        #            self.api_url = row['url']
        #            self.api_key = row['api']
        #except Exception as e:
        #    QMessageBox.critical(self, "Fehler", f"Konfigurationsdatei fehlerhaft: {str(e)}")

        # UI Setup
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.output_splitter = QSplitter(Qt.Vertical)

        self.transcript_textedit = QTextEdit()
        self.transcript_textedit.setReadOnly(True)
        self.transcript_textedit.setPlaceholderText("Transkripte erscheinen hier...")

        self.help_browser = QTextBrowser()
        try:
            with open('help.txt', 'r', encoding='utf-8') as f:
                help_content = f.read()
                help_html = markdown.markdown(help_content)
                self.help_browser.setHtml(help_html)
        except Exception as e:
            self.help_browser.setPlainText(f"Fehler beim Laden der Hilfe: {str(e)}")

        self.output_splitter.addWidget(self.transcript_textedit)
        self.output_splitter.addWidget(self.help_browser)

        # Input fields for 5 URLs
        self.control_panel = QWidget()
        control_layout = QVBoxLayout()

        self.link_inputs = []
        for i in range(5):
            le = QLineEdit()
            le.setPlaceholderText(f"YouTube-Link {i + 1}")
            self.link_inputs.append(le)
            control_layout.addWidget(le)

        self.holen_button = QPushButton("Transkripte holen")
        self.speichern_button = QPushButton("Transkript speichern")  # Neuer Button

        control_layout.addWidget(self.holen_button)
        control_layout.addWidget(self.speichern_button)  # Button hinzugefügt
        control_layout.addStretch()
        self.control_panel.setLayout(control_layout)

        self.main_splitter.addWidget(self.output_splitter)
        self.main_splitter.addWidget(self.control_panel)
        self.setCentralWidget(self.main_splitter)

        # Connections
        self.holen_button.clicked.connect(self.fetch_transcript)
        self.speichern_button.clicked.connect(self.save_transcript)  # Verbindung

        self.transcript_text = ""

    def extract_video_id(self, url):
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Ungültiger YouTube-Link")

    def fetch_transcript(self):
        self.transcript_text = ""
        transcripts = []

        for le in self.link_inputs:
            url = le.text().strip()
            if not url:
                continue

            try:
                video_id = self.extract_video_id(url)
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                transcript = " ".join([entry["text"].replace('\n', ' ') for entry in transcript_list])
                transcripts.append(transcript)
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"Fehler bei {url}:\n{e}")

        # Join transcripts with paragraph separation
        self.transcript_text = "\n\n".join(transcripts)
        self.transcript_textedit.setPlainText(self.transcript_text)

    def save_transcript(self):
        if not self.transcript_text:
            QMessageBox.warning(self, "Warnung", "Kein Transkript zum Speichern vorhanden")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Transkript speichern", "", "Text Files (*.txt)"
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.transcript_text)
                QMessageBox.information(self, "Erfolg", "Transkript erfolgreich gespeichert")
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Speichern fehlgeschlagen: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
