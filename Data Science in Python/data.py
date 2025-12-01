import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import pandas as pd
import numpy as np
import joblib
import os
import base64
import io

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Constants
MODEL_DIR = "train_save_model"
os.makedirs(MODEL_DIR, exist_ok=True)

feature_cols = [
    'age', 'gender', 'blood_pressure', 'cholesterol', 'blood_sugar', 'restecg',
    'max_heart_rate', 'exang', 'st_depression', 'slope', 'ca', 'thal',
    'smoking_habits', 'cp_1', 'cp_2', 'cp_3'
]

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(probability=True),
    "KNN": KNeighborsClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Neural Network": MLPClassifier(max_iter=1000)
}

external_stylesheets = [dbc.themes.SANDSTONE, "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Heart Disease Risk Prediction"

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background-color: #f7f7f7;
            }
            .dash-container {
                padding: 30px;
                background: white;
                border-radius: 12px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            }
            h1 {
                font-weight: 700;
                color: #2c3e50;
            }
            .btn {
                width: 100%;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

df_storage = {}

# === Data Functions ===
def preprocess_data(df):
    df = df[feature_cols + ['heart_disease']].dropna()
    X = df[feature_cols].apply(pd.to_numeric, errors='coerce').fillna(0)
    y = df['heart_disease']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler

def classify(df, model_name):
    X, y, scaler = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = models[model_name]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = f"""
Model: {model_name}  
Accuracy: {accuracy_score(y_test, y_pred):.4f}  
Precision: {precision_score(y_test, y_pred):.4f}  
Recall: {recall_score(y_test, y_pred):.4f}  
F1 Score: {f1_score(y_test, y_pred):.4f}  
"""
    return metrics, (model, scaler)

def save_model(model_and_scaler, model_name):
    filename = os.path.join(MODEL_DIR, f"{model_name.replace(' ', '_').lower()}_model.pkl")
    joblib.dump(model_and_scaler, filename)
    return f"Model saved to {filename}"

def load_model(model_name):
    filename = os.path.join(MODEL_DIR, f"{model_name.replace(' ', '_').lower()}_model.pkl")
    if not os.path.exists(filename):
        return None
    return joblib.load(filename)

def predict_risk(model_name, inputs):
    model_and_scaler = load_model(model_name)
    if model_and_scaler is None:
        return "Model not found."
    try:
        inputs = [float(val) for val in inputs]
    except:
        return "Please provide valid numeric inputs."
    model, scaler = model_and_scaler
    X_scaled = scaler.transform(np.array(inputs).reshape(1, -1))
    prediction = model.predict(X_scaled)[0]
    proba = model.predict_proba(X_scaled)[0][1] if hasattr(model, "predict_proba") else None
    result = "High Risk" if prediction == 1 else "Low Risk"
    if proba is not None:
        result += f" (Probability: {proba:.2f})"
    return result

def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    return df

# === Layout ===
app.layout = dbc.Container([
    html.Div([
        html.H1("Cardiovascular Disease Prediction App", className="text-center mb-4"),
        dcc.Tabs([
            dcc.Tab(label="Train Model", children=[
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='train-model-dropdown', options=[{'label': k, 'value': k} for k in models], value='Logistic Regression'),
                        dcc.Upload(id='train-upload', children=html.Div(['Drag & Drop or ', html.A('Select CSV File')]), multiple=False,
                                   style={'border': '2px dashed #ccc', 'padding': '10px', 'margin-top': '10px'}),
                        html.Button("Train Model", id="train-btn", n_clicks=0, className="btn btn-primary mt-2"),
                        html.Div(id="train-result", className="mt-3"),
                        html.Button("Save Model", id="save-model-btn", n_clicks=0, className="btn btn-success mt-2"),
                        html.Div(id="save-model-msg", className="mt-2")
                    ])
                ])
            ]),
            dcc.Tab(label="Compare Models", children=[
                dbc.Row([
                    dbc.Col([
                        dcc.Upload(id='compare-upload', children=html.Div(['Drag & Drop or ', html.A('Select CSV File')]), multiple=False,
                                   style={'border': '2px dashed #ccc', 'padding': '10px', 'margin-top': '10px'}),
                        html.Button("Compare Models", id="compare-btn", n_clicks=0, className="btn btn-secondary mt-2"),
                        html.Pre(id="compare-result", className="mt-2")
                    ])
                ])
            ]),
            dcc.Tab(label="Cross Validation", children=[
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='cv-model-dropdown', options=[{'label': k, 'value': k} for k in models], value='Logistic Regression'),
                        dcc.Upload(id='cv-upload', children=html.Div(['Drag & Drop or ', html.A('Select CSV File')]), multiple=False,
                                   style={'border': '2px dashed #ccc', 'padding': '10px', 'margin-top': '10px'}),
                        html.Button("Run Cross Validation", id="cv-btn", n_clicks=0, className="btn btn-warning mt-2"),
                        html.Pre(id="cv-result", className="mt-2")
                    ])
                ])
            ]),
            dcc.Tab(label="Risk Prediction", children=[
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(id='predict-model-dropdown', options=[{'label': k, 'value': k} for k in models], value='Logistic Regression'),
                        html.Div([
                            dbc.Input(id=f"input-{col}", placeholder=col, type="text", className="mb-2") for col in feature_cols
                        ]),
                        html.Button("Predict Risk", id="predict-btn", n_clicks=0, className="btn btn-danger mt-2"),
                        html.Div(id="predict-result", className="mt-3")
                    ])
                ])
            ])
        ])
    ], className="dash-container")
], fluid=True)

# === Callbacks ===
@app.callback(
    Output("train-result", "children"),
    Input("train-btn", "n_clicks"),
    State("train-upload", "contents"),
    State("train-upload", "filename"),
    State("train-model-dropdown", "value"),
    prevent_initial_call=True
)
def train_model(n_clicks, contents, filename, model_name):
    if contents is None:
        return "Please upload a CSV file to train."
    try:
        df = parse_contents(contents)
        metrics, model_and_scaler = classify(df, model_name)
        df_storage['trained'] = (model_name, model_and_scaler)
        return metrics
    except Exception as e:
        return f"Error during training: {str(e)}"

@app.callback(
    Output("save-model-msg", "children"),
    Input("save-model-btn", "n_clicks"),
    prevent_initial_call=True
)
def save_model_callback(n_clicks):
    if 'trained' not in df_storage:
        return "Train a model first!"
    model_name, model_and_scaler = df_storage['trained']
    msg = save_model(model_and_scaler, model_name)
    return msg

@app.callback(
    Output("compare-result", "children"),
    Input("compare-btn", "n_clicks"),
    State("compare-upload", "contents"),
    prevent_initial_call=True
)
def compare_models_callback(n_clicks, contents):
    if contents is None:
        return "Please upload a CSV file to compare models."
    try:
        df = parse_contents(contents)
        X, y, _ = preprocess_data(df)
        output = ""
        for name, model in models.items():
            scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
            output += f"{name}: Accuracy = {scores.mean():.4f} (\u00b1 {scores.std():.4f})\n"
        return output
    except Exception as e:
        return f"Error: {str(e)}"

@app.callback(
    Output("cv-result", "children"),
    Input("cv-btn", "n_clicks"),
    State("cv-upload", "contents"),
    State("cv-model-dropdown", "value"),
    prevent_initial_call=True
)
def cross_validation_callback(n_clicks, contents, model_name):
    if contents is None:
        return "Please upload a CSV file to run cross validation."
    try:
        df = parse_contents(contents)
        X, y, _ = preprocess_data(df)
        model = models[model_name]
        scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
        return f"{model_name} Cross-Validation Accuracy: {scores.mean():.4f} (\u00b1 {scores.std():.4f})"
    except Exception as e:
        return f"Error: {str(e)}"

@app.callback(
    Output("predict-result", "children"),
    Input("predict-btn", "n_clicks"),
    State("predict-model-dropdown", "value"),
    *[State(f"input-{col}", "value") for col in feature_cols],
    prevent_initial_call=True
)
def predict_callback(n_clicks, model_name, *inputs):
    if None in inputs or "" in inputs:
        return "Please fill in all input fields."
    result = predict_risk(model_name, inputs)
    return f"Prediction Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)
