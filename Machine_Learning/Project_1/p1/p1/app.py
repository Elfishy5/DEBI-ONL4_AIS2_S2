import dash
from dash import dcc, html, Input, Output, State
import pickle
import numpy as np
import os

# تحديد المسار الدقيق للملف بناءً على مكان سكريبت app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'boston_model.pkl')

# 1. تحميل الموديل المحفوظ
with open(model_path, 'rb') as file:
    model = pickle.load(file)


# 2. تهيئة التطبيق
app = dash.Dash(__name__)

# 3. تصميم الواجهة (Layout)
app.layout = html.Div([
    html.H1("Boston Housing Price Predictor", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Div([
        html.Label("Number of Rooms (RM):"),
        dcc.Input(id='rm-input', type='number', value=5, step=1, style={'margin': '10px'})
    ], style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Neighborhood Poverty Level (LSTAT):"),
        dcc.Input(id='lstat-input', type='number', value=34, step=1, style={'margin': '10px'})
    ], style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Student-Teacher Ratio (PTRATIO):"),
        dcc.Input(id='ptratio-input', type='number', value=15, step=1, style={'margin': '10px'})
    ], style={'textAlign': 'center'}),
    
    html.Div([
        html.Button('Predict Price', id='predict-btn', n_clicks=0, 
                    style={'fontSize': '18px', 'padding': '10px 20px', 'backgroundColor': '#2980b9', 'color': 'white', 'border': 'none', 'borderRadius': '5px'})
    ], style={'textAlign': 'center', 'marginTop': '20px'}),
    
    # مكان عرض النتيجة
    html.H2(id='output-prediction', style={'textAlign': 'center', 'color': '#27ae60', 'marginTop': '30px'})
], style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '600px', 'margin': 'auto', 'padding': '20px'})

# 4. برمجة التفاعل (Callback)
@app.callback(
    Output('output-prediction', 'children'),
    Input('predict-btn', 'n_clicks'),
    State('rm-input', 'value'),
    State('lstat-input', 'value'),
    State('ptratio-input', 'value')
)
def update_prediction(n_clicks, rm, lstat, ptratio):
    if n_clicks > 0:
        # التأكد من عدم وجود حقول فارغة
        if rm is None or lstat is None or ptratio is None:
            return "Please fill in all fields."
        
        # تجهيز البيانات بنفس شكل المصفوفة التي تدرب عليها الموديل
        input_features = np.array([[rm, lstat, ptratio]])
        
        # عمل التوقع
        prediction = model.predict(input_features)[0]
        
        # تنسيق النتيجة كعملة
        return f"Predicted Selling Price: ${prediction:,.2f}"
    
    return ""

# 5. تشغيل السيرفر
if __name__ == '__main__':
    app.run(debug=True)