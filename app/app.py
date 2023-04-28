from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mindmap')
def mindmap():
    nodes = [
        {"id": "1", "label": "Node 1"},
        {"id": "2", "label": "Node 2"},
        {"id": "3", "label": "Node 3"},
        {"id": "4", "label": "Node 4"},
        {"id": "5", "label": "Node 5"},
        {"id": "6", "label": "Node 6"}
    ]
    edges = [
        {"from": "1", "to": "2"},
        {"from": "1", "to": "3"},
        {"from": "2", "to": "4"},
        {"from": "2", "to": "5"},
        {"from": "3", "to": "6"}
    ]
    return render_template('mindmap.html', nodes=nodes, edges=edges)