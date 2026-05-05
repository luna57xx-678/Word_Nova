import sys
import os
import json
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QToolBar, QComboBox, QSpinBox, QColorDialog, QFileDialog,
    QMessageBox, QSplitter, QPushButton, QLabel, QStatusBar, QFontComboBox,
    QStyleFactory, QDialog
)
from PyQt5.QtCore import Qt, QTimer, QUrl, pyqtSignal
from PyQt5.QtGui import (
    QFont, QColor, QIcon, QTextCursor, QTextCharFormat, 
    QTextBlockFormat, QTextDocument, QTextListFormat
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl as CoreUrl


class EntryUI(QDialog):
    """Entry UI window with crescent moon and Enter Word Nova button"""
    entry_accepted = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Word Nova - Crescent Studios')
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet(self.load_css())
        
        # Set window icon and properties
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create web view to render the entry UI
        web_view = QWebEngineView()
        html_content = self.get_entry_html()
        web_view.setHtml(html_content)
        
        layout.addWidget(web_view)
        self.setLayout(layout)

    def load_css(self):
        """Load CSS for the entry UI"""
        css_file = os.path.join(os.path.dirname(__file__), 'entry-ui.css')
        if os.path.exists(css_file):
            with open(css_file, 'r') as f:
                return f.read()
        return ""

    def get_entry_html(self):
        """Generate HTML for entry UI"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    overflow: hidden;
                    position: relative;
                }

                body::before {
                    content: '';
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-image: 
                        radial-gradient(2px 2px at 20px 30px, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0)),
                        radial-gradient(2px 2px at 60px 70px, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0)),
                        radial-gradient(1px 1px at 50px 50px, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0)),
                        radial-gradient(1px 1px at 130px 80px, rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0)),
                        radial-gradient(2px 2px at 90px 10px, rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0));
                    background-repeat: repeat;
                    background-size: 200px 200px;
                    pointer-events: none;
                    z-index: 1;
                    opacity: 0.5;
                    animation: float 20s infinite linear;
                }

                @keyframes float {
                    0% { transform: translateY(0px); }
                    100% { transform: translateY(20px); }
                }

                .entry-container {
                    position: relative;
                    z-index: 10;
                    text-align: center;
                    max-width: 600px;
                    padding: 40px;
                }

                .entry-card {
                    background: rgba(30, 30, 30, 0.8);
                    backdrop-filter: blur(10px);
                    border-radius: 20px;
                    padding: 60px 40px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3),
                                inset 0 1px 1px rgba(255, 255, 255, 0.2);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    animation: slideUp 0.8s ease-out;
                }

                @keyframes slideUp {
                    from {
                        opacity: 0;
                        transform: translateY(30px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                .moon-container {
                    position: relative;
                    width: 200px;
                    height: 200px;
                    margin: 0 auto 40px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .moon-glow {
                    position: absolute;
                    width: 220px;
                    height: 220px;
                    border-radius: 50%;
                    background: radial-gradient(circle, rgba(138, 43, 226, 0.3) 0%, transparent 70%);
                    animation: pulse 3s ease-in-out infinite;
                    z-index: 1;
                }

                @keyframes pulse {
                    0%, 100% {
                        box-shadow: 0 0 30px rgba(138, 43, 226, 0.5),
                                    0 0 60px rgba(138, 43, 226, 0.3);
                    }
                    50% {
                        box-shadow: 0 0 50px rgba(138, 43, 226, 0.7),
                                    0 0 80px rgba(138, 43, 226, 0.4);
                    }
                }

                .crescent-moon {
                    position: relative;
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #f0f0f0 0%, #ffffff 50%, #e8e8e8 100%);
                    box-shadow: -10px 10px 20px rgba(0, 0, 0, 0.4),
                                inset 5px -5px 10px rgba(0, 0, 0, 0.1);
                    z-index: 3;
                    animation: moonFloat 4s ease-in-out infinite;
                }

                @keyframes moonFloat {
                    0%, 100% {
                        transform: translateY(0px) rotate(0deg);
                    }
                    50% {
                        transform: translateY(-10px) rotate(2deg);
                    }
                }

                .crescent-moon::before {
                    content: '';
                    position: absolute;
                    width: 140px;
                    height: 140px;
                    border-radius: 50%;
                    background: rgba(30, 30, 30, 0.8);
                    top: 50%;
                    left: 50%;
                    transform: translate(-55%, -50%);
                    box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.5);
                }

                .star {
                    position: absolute;
                    width: 4px;
                    height: 4px;
                    background: white;
                    border-radius: 50%;
                    opacity: 0;
                    animation: twinkle 3s ease-in-out infinite;
                }

                .star:nth-child(1) {
                    top: 20px;
                    left: 80px;
                    animation-delay: 0s;
                }

                .star:nth-child(2) {
                    top: 30px;
                    right: 40px;
                    animation-delay: 0.5s;
                }

                .star:nth-child(3) {
                    bottom: 40px;
                    right: 30px;
                    animation-delay: 1s;
                }

                .star:nth-child(4) {
                    bottom: 50px;
                    left: 50px;
                    animation-delay: 1.5s;
                }

                @keyframes twinkle {
                    0%, 100% { opacity: 0; }
                    50% { opacity: 1; }
                }

                .studio-name {
                    margin-top: 50px;
                    position: relative;
                    z-index: 10;
                }

                .studio-name h2 {
                    font-size: 32px;
                    font-weight: 700;
                    background: linear-gradient(135deg, #8a2be2 0%, #da70d6 50%, #ff1493 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                    margin-bottom: 10px;
                    letter-spacing: 2px;
                    animation: fadeInDown 0.8s ease-out 0.2s both;
                }

                @keyframes fadeInDown {
                    from {
                        opacity: 0;
                        transform: translateY(-20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                .studio-name p {
                    font-size: 13px;
                    color: rgba(255, 255, 255, 0.6);
                    letter-spacing: 3px;
                    text-transform: uppercase;
                    font-weight: 600;
                    animation: fadeInDown 0.8s ease-out 0.3s both;
                }

                .enter-button {
                    margin-top: 50px;
                    position: relative;
                    z-index: 10;
                }

                .btn-enter {
                    position: relative;
                    padding: 16px 50px;
                    font-size: 18px;
                    font-weight: 700;
                    letter-spacing: 1px;
                    text-transform: uppercase;
                    color: white;
                    background: linear-gradient(135deg, #8a2be2 0%, #da70d6 100%);
                    border: 2px solid transparent;
                    border-radius: 50px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    overflow: hidden;
                    box-shadow: 0 4px 15px rgba(138, 43, 226, 0.4),
                                0 0 20px rgba(138, 43, 226, 0.2);
                    animation: fadeInUp 0.8s ease-out 0.4s both;
                }

                @keyframes fadeInUp {
                    from {
                        opacity: 0;
                        transform: translateY(20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                .btn-enter:hover {
                    transform: translateY(-3px);
                    box-shadow: 0 8px 25px rgba(138, 43, 226, 0.6),
                                0 0 30px rgba(138, 43, 226, 0.4),
                                inset 0 0 20px rgba(255, 255, 255, 0.1);
                    border-color: rgba(255, 255, 255, 0.3);
                }

                .btn-enter:active {
                    transform: translateY(-1px);
                    box-shadow: 0 4px 15px rgba(138, 43, 226, 0.4);
                }

                @media (max-width: 768px) {
                    .entry-card { padding: 40px 30px; }
                    .moon-container { width: 160px; height: 160px; }
                    .crescent-moon { width: 120px; height: 120px; }
                    .crescent-moon::before { width: 110px; height: 110px; }
                    .studio-name h2 { font-size: 24px; }
                    .btn-enter { padding: 14px 40px; font-size: 16px; }
                }
            </style>
        </head>
        <body>
            <div class="entry-container">
                <div class="entry-card">
                    <div class="moon-container">
                        <div class="moon-glow"></div>
                        <div class="crescent-moon">
                            <div class="star"></div>
                            <div class="star"></div>
                            <div class="star"></div>
                            <div class="star"></div>
                        </div>
                    </div>
                    
                    <div class="studio-name">
                        <h2>Crescent Studios</h2>
                        <p>Word Nova</p>
                    </div>

                    <div class="enter-button">
                        <button class="btn-enter" onclick="enterWordNova()">Enter Word Nova</button>
                    </div>
                </div>
            </div>

            <script>
                function enterWordNova() {
                    window.location.href = 'about:blank';
                }
            </script>
        </body>
        </html>
        """
        return html


class WordNovaEditor(QMainWindow):
    """Main Word Nova Editor with MS Word-like features"""

    def __init__(self):
        super().__init__()
        self.autosave_timer = None
        self.current_file = None
        self.is_modified = False
        self.autosave_dir = os.path.join(os.path.expanduser('~'), '.word_nova')
        
        # Create autosave directory
        os.makedirs(self.autosave_dir, exist_ok=True)
        
        self.initUI()
        self.start_autosave()

    def initUI(self):
        """Initialize the main editor UI"""
        self.setWindowTitle('Word Nova - Document Editor')
        self.setGeometry(50, 50, 1200, 800)
        
        # Set dark theme
        self.setStyle(QStyleFactory.create('Fusion'))
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create toolbar
        self.create_toolbar()
        
        # Create text editor
        self.text_editor = QTextEdit()
        self.text_editor.setFont(QFont('Calibri', 12))
        self.text_editor.textChanged.connect(self.on_text_changed)
        
        main_layout.addWidget(self.text_editor)
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Ready | Autosave: Enabled')

    def create_toolbar(self):
        """Create comprehensive toolbar with formatting options"""
        # File toolbar
        file_toolbar = self.addToolBar('File')
        file_toolbar.setMovable(False)
        
        new_btn = QPushButton('📄 New')
        new_btn.clicked.connect(self.new_document)
        file_toolbar.addWidget(new_btn)
        
        open_btn = QPushButton('📂 Open')
        open_btn.clicked.connect(self.open_document)
        file_toolbar.addWidget(open_btn)
        
        save_btn = QPushButton('💾 Save')
        save_btn.clicked.connect(self.save_document)
        file_toolbar.addWidget(save_btn)
        
        file_toolbar.addSeparator()
        
        # Format toolbar
        format_toolbar = self.addToolBar('Format')
        format_toolbar.setMovable(False)
        
        # Font selection
        self.font_combo = QFontComboBox()
        self.font_combo.setCurrentFont(QFont('Calibri'))
        self.font_combo.currentFontChanged.connect(self.change_font)
        format_toolbar.addWidget(QLabel('Font:'))
        format_toolbar.addWidget(self.font_combo)
        
        format_toolbar.addSeparator()
        
        # Font size
        self.size_spinbox = QSpinBox()
        self.size_spinbox.setValue(12)
        self.size_spinbox.setMinimum(8)
        self.size_spinbox.setMaximum(72)
        self.size_spinbox.valueChanged.connect(self.change_font_size)
        format_toolbar.addWidget(QLabel('Size:'))
        format_toolbar.addWidget(self.size_spinbox)
        
        format_toolbar.addSeparator()
        
        # Bold button
        bold_btn = QPushButton('𝐁 Bold')
        bold_btn.clicked.connect(self.toggle_bold)
        format_toolbar.addWidget(bold_btn)
        
        # Italic button
        italic_btn = QPushButton('𝘐 Italic')
        italic_btn.clicked.connect(self.toggle_italic)
        format_toolbar.addWidget(italic_btn)
        
        # Underline button
        underline_btn = QPushButton('U Underline')
        underline_btn.clicked.connect(self.toggle_underline)
        format_toolbar.addWidget(underline_btn)
        
        format_toolbar.addSeparator()
        
        # Text color
        color_btn = QPushButton('🎨 Color')
        color_btn.clicked.connect(self.change_text_color)
        format_toolbar.addWidget(color_btn)
        
        format_toolbar.addSeparator()
        
        # Alignment buttons
        left_align_btn = QPushButton('⬅ Left')
        left_align_btn.clicked.connect(self.align_left)
        format_toolbar.addWidget(left_align_btn)
        
        center_align_btn = QPushButton('⬇ Center')
        center_align_btn.clicked.connect(self.align_center)
        format_toolbar.addWidget(center_align_btn)
        
        right_align_btn = QPushButton('➡ Right')
        right_align_btn.clicked.connect(self.align_right)
        format_toolbar.addWidget(right_align_btn)
        
        format_toolbar.addSeparator()
        
        # List buttons
        bullet_btn = QPushButton('• Bullet')
        bullet_btn.clicked.connect(self.add_bullet_list)
        format_toolbar.addWidget(bullet_btn)
        
        numbered_btn = QPushButton('1. Numbered')
        numbered_btn.clicked.connect(self.add_numbered_list)
        format_toolbar.addWidget(numbered_btn)

    def new_document(self):
        """Create a new document"""
        if self.text_editor.document().isModified():
            reply = QMessageBox.question(
                self, 'Save Document?',
                'Do you want to save the current document?',
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.save_document()
            elif reply == QMessageBox.Cancel:
                return
        
        self.text_editor.clear()
        self.current_file = None
        self.setWindowTitle('Word Nova - Document Editor [Untitled]')
        self.is_modified = False

    def open_document(self):
        """Open an existing document"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open Document', '',
            'Word Documents (*.docx);;Text Files (*.txt);;All Files (*.*)'
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.text_editor.setText(content)
                    self.current_file = file_path
                    self.setWindowTitle(f'Word Nova - {os.path.basename(file_path)}')
                    self.is_modified = False
                    self.status_bar.showMessage(f'Opened: {file_path}')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to open file: {str(e)}')

    def save_document(self):
        """Save the current document"""
        if not self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(
                self, 'Save Document', '',
                'Word Documents (*.docx);;Text Files (*.txt);;All Files (*.*)'
            )
            if not file_path:
                return
            self.current_file = file_path
        
        try:
            with open(self.current_file, 'w', encoding='utf-8') as f:
                f.write(self.text_editor.toPlainText())
            self.setWindowTitle(f'Word Nova - {os.path.basename(self.current_file)}')
            self.is_modified = False
            self.status_bar.showMessage(f'Saved: {self.current_file}')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save file: {str(e)}')

    def autosave_document(self):
        """Automatically save the document"""
        if self.is_modified:
            autosave_file = os.path.join(self.autosave_dir, 'autosave.txt')
            try:
                with open(autosave_file, 'w', encoding='utf-8') as f:
                    f.write(self.text_editor.toPlainText())
                
                # Save metadata
                metadata_file = os.path.join(self.autosave_dir, 'metadata.json')
                metadata = {
                    'last_saved': datetime.now().isoformat(),
                    'file_path': self.current_file,
                    'is_modified': self.is_modified
                }
                with open(metadata_file, 'w') as f:
                    json.dump(metadata, f)
                
                self.status_bar.showMessage('Autosaved')
            except Exception as e:
                print(f'Autosave failed: {str(e)}')

    def start_autosave(self):
        """Start the autosave timer (every 30 seconds)"""
        self.autosave_timer = QTimer()
        self.autosave_timer.timeout.connect(self.autosave_document)
        self.autosave_timer.start(30000)  # 30 seconds

    def on_text_changed(self):
        """Handle text changes"""
        self.is_modified = True

    def change_font(self, font):
        """Change the font of selected text"""
        cursor = self.text_editor.textCursor()
        if not cursor.hasSelection():
            return
        
        fmt = QTextCharFormat()
        fmt.setFont(font)
        cursor.mergeCharFormat(fmt)

    def change_font_size(self, size):
        """Change the font size"""
        cursor = self.text_editor.textCursor()
        if not cursor.hasSelection():
            return
        
        fmt = QTextCharFormat()
        fmt.setFontPointSize(size)
        cursor.mergeCharFormat(fmt)

    def toggle_bold(self):
        """Toggle bold formatting"""
        cursor = self.text_editor.textCursor()
        if not cursor.hasSelection():
            return
        
        fmt = QTextCharFormat()
        fmt.setFontWeight(600 if not cursor.charFormat().fontWeight() == 600 else 400)
        cursor.mergeCharFormat(fmt)

    def toggle_italic(self):
        """Toggle italic formatting"""
        cursor = self.text_editor.textCursor()
        if not cursor.hasSelection():
            return
        
        fmt = QTextCharFormat()
        fmt.setFontItalic(not cursor.charFormat().fontItalic())
        cursor.mergeCharFormat(fmt)

    def toggle_underline(self):
        """Toggle underline formatting"""
        cursor = self.text_editor.textCursor()
        if not cursor.hasSelection():
            return
        
        fmt = QTextCharFormat()
        fmt.setFontUnderline(not cursor.charFormat().fontUnderline())
        cursor.mergeCharFormat(fmt)

    def change_text_color(self):
        """Change text color"""
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.text_editor.textCursor()
            if not cursor.hasSelection():
                return
            
            fmt = QTextCharFormat()
            fmt.setForeground(color)
            cursor.mergeCharFormat(fmt)

    def align_left(self):
        """Align text left"""
        fmt = QTextBlockFormat()
        fmt.setAlignment(Qt.AlignLeft)
        self.text_editor.textCursor().mergeBlockFormat(fmt)

    def align_center(self):
        """Align text center"""
        fmt = QTextBlockFormat()
        fmt.setAlignment(Qt.AlignCenter)
        self.text_editor.textCursor().mergeBlockFormat(fmt)

    def align_right(self):
        """Align text right"""
        fmt = QTextBlockFormat()
        fmt.setAlignment(Qt.AlignRight)
        self.text_editor.textCursor().mergeBlockFormat(fmt)

    def add_bullet_list(self):
        """Add bullet list formatting"""
        cursor = self.text_editor.textCursor()
        list_fmt = QTextListFormat()
        list_fmt.setStyle(QTextListFormat.ListDisc)
        cursor.insertList(list_fmt)

    def add_numbered_list(self):
        """Add numbered list formatting"""
        cursor = self.text_editor.textCursor()
        list_fmt = QTextListFormat()
        list_fmt.setStyle(QTextListFormat.ListDecimal)
        cursor.insertList(list_fmt)


class Application(QApplication):
    """Main application class"""

    def __init__(self, argv):
        super().__init__(argv)
        self.entry_window = None
        self.editor_window = None
        self.show_entry_ui()

    def show_entry_ui(self):
        """Show the entry UI"""
        self.entry_window = EntryUI()
        self.entry_window.finished.connect(self.on_entry_accepted)
        self.entry_window.show()

    def on_entry_accepted(self):
        """Handle entry UI acceptance"""
        self.entry_window.close()
        self.show_editor()

    def show_editor(self):
        """Show the main editor"""
        self.editor_window = WordNovaEditor()
        self.editor_window.show()


def main():
    app = Application(sys.argv)
    
    # Handle the entry UI button click
    # Using a timer to detect when entry UI should be closed
    def check_entry_close():
        if app.entry_window and app.entry_window.isVisible():
            return
        app.on_entry_accepted()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
