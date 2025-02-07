import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# CSV 파일 로드 및 전처리
def open_csv():
    df = pd.read_csv('human_vital_signs_dataset_2024.csv', encoding='utf-8')

    # 필요한 컬럼만 선택
    df = df[['Heart Rate', 'Respiratory Rate', 'Body Temperature', 'Age', 'Gender',
             'Systolic Blood Pressure', 'Diastolic Blood Pressure', 'Risk Category']]

    # 범주형 변수 'Gender' 처리: Male: 0, Female: 1
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    # 'Risk Category'를 0 (Low Risk)과 1 (High Risk)로 변환
    df['Risk Category'] = df['Risk Category'].map({'Low Risk': 0, 'High Risk': 1})

    print(df.isnull().sum())  # 결측값 확인

    return df

# XGBoost 모델로 학습 및 예측
def XGBoost_Model(df):
    # feature와 target 분리
    features = ['Heart Rate', 'Respiratory Rate', 'Body Temperature', 'Age', 'Gender',
                'Systolic Blood Pressure', 'Diastolic Blood Pressure']
    target = 'Risk Category'

    x = df[features]
    y = df[target]

    # 결측값 처리 (평균값으로 대체)
    imputer = SimpleImputer(strategy="mean")
    x = imputer.fit_transform(x)

    # 데이터 표준화 (스케일링)
    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    # 데이터 분할 (훈련 데이터: 80%, 테스트 데이터: 20%)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print(f'훈련 샘플 수: {x_train.shape[0]}, 테스트 샘플 수: {x_test.shape[0]}')

    # XGBoost 모델 학습
    xgb = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
    xgb.fit(x_train, y_train)

    # 예측 수행
    y_pred = xgb.predict(x_test)
    acc = accuracy_score(y_test, y_pred)

    print(f'XGBoost 모델 정확도: {acc:.4f}')

    return xgb, acc

# 예측 실행
def predict_risk(model, input_data):
    # 결측값 처리 및 데이터 표준화
    imputer = SimpleImputer(strategy="mean")
    input_data = imputer.fit_transform([input_data])  # 입력 데이터에 결측값이 있을 수 있어 처리
    scaler = StandardScaler()
    input_data = scaler.fit_transform(input_data)

    # 예측
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        return "Low Risk"
    else:
        return "High Risk"


def read_dataset(vital):
    df = open_csv()
    model, accuracy = XGBoost_Model(df)
    result = predict_risk(model, vital)
    print(result)
    return result
    # # 사용자 입력 받기
    # user_input = get_user_input()
    # if user_input:
    #     # 사용자 입력으로 예측
    #     result = predict_risk(model, user_input)
    #     print(f"The predicted risk category is: {result}")
