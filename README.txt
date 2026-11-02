MiniLex – Visual Lexical Analyzer

Requirements:
- Python 3.9 or newer
- Flask

Run locally:
1. Extract this ZIP.
2. Open terminal/command prompt in the project folder.
3. Install Flask: python -m pip install -r requirements.txt
4. Start: python app.py
5. Open http://127.0.0.1:5000 in your browser.

Features:
- Keyword, identifier, number, operator and delimiter recognition
- Token stream with line numbers
- Invalid character reporting
- Educational NFA/DFA state-flow illustration

Important: The NFA/DFA panel is a simple illustrative state flow, not a full automatic NFA-to-DFA construction engine.
