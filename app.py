from flask import Flask, render_template, request
import re

app = Flask(__name__)

KEYWORDS = {
    "int", "float", "char", "double", "if", "else", "while",
    "for", "return", "void", "main", "printf", "scanf"
}

TOKEN_SPEC = [
    ("COMMENT", r"//[^\n]*|/\*[\s\S]*?\*/"),
    ("NUMBER", r"\d+(?:\.\d+)?"),
    ("IDENTIFIER", r"[A-Za-z_][A-Za-z0-9_]*"),
    ("OPERATOR", r"==|!=|<=|>=|\+\+|--|&&|\|\||[+\-*/%=<>!]"),
    ("DELIMITER", r"[(){}\[\];,]"),
    ("NEWLINE", r"\n"),
    ("WHITESPACE", r"[ \t\r]+"),
    ("MISMATCH", r"."),
]

MASTER_REGEX = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))


def analyze(code):
    tokens, errors = [], []
    line_num = 1
    for match in MASTER_REGEX.finditer(code):
        kind, lexeme = match.lastgroup, match.group()
        if kind == "NEWLINE":
            line_num += 1
        elif kind in ("WHITESPACE", "COMMENT"):
            continue
        elif kind == "IDENTIFIER" and lexeme in KEYWORDS:
            tokens.append({"line": line_num, "lexeme": lexeme, "token": "KEYWORD"})
        elif kind == "MISMATCH":
            errors.append({"line": line_num, "lexeme": lexeme, "message": f"Invalid character: {lexeme}"})
        else:
            tokens.append({"line": line_num, "lexeme": lexeme, "token": kind})
    return tokens, errors


@app.route("/", methods=["GET", "POST"])
def index():
    code, tokens, errors = "", [], []
    if request.method == "POST":
        code = request.form.get("code", "")
        tokens, errors = analyze(code)
    return render_template("index.html", code=code, tokens=tokens, errors=errors)


if __name__ == "__main__":
    app.run(debug=True)
