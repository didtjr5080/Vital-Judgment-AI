from flask import Flask, render_template, request
import ReadDataset
import ollama_api

app = Flask(__name__)

@app.route('/main')
def index():
    return render_template('main.html')

@app.route('/submit', methods=['POST'])
def submit():
    # HTML에서 사용된 name 속성에 맞춰 변수명을 수정
    bpmax = request.form.get('BP_Max')  # 대소문자 일치
    bpmin = request.form.get('BP_Min')
    temp = request.form.get('temperleture')  # 철자 그대로 맞추기
    pulse = request.form.get('pusle')
    br = request.form.get('breath')
    gender = request.form.get('gender')
    age = request.form.get('age')

    # 값 확인 (디버깅)
    print(f"bpmax: {bpmax}, bpmin: {bpmin}, temp: {temp}, pulse: {pulse}, br: {br}, gendr: {gender}, age: {age}")

    # 값이 없을 경우 오류 메시지 출력
    if not all([bpmax, bpmin, temp, pulse, br, gender, age]):
        return f" 모두 입력해주세요!<br>bpmax: {bpmax}, bpmin: {bpmin}, temp: {temp}, pulse: {pulse}, br: {br}, gendr: {gender}, age: {age}", 400

    result_michin = ReadDataset.read_dataset([bpmax, bpmin, temp, pulse, br, gender, age])
    if result_michin == 'Low Risk':
        result_michin = '머신러닝 데이터 결과: 안전하다고 예측됨'
    elif result_michin == 'High Risk':
        result_michin = '머신러닝 데이터 결과: 위독한 상황이라고 예측됨'

    if gender == '1':
        gender = 'female'
    elif gender == '0':
        gender = 'male'
    thrrow = f"BP: {bpmax}/{bpmin}, Temperature: {temp}, Pulse: {pulse}, Breath: {br}, gendr: {gender}, age: {age}"
    result = ollama_api.ollama_result(thrrow)
    result = result.replace('\n', '<br>')
    result = result_michin+ '<br><br>' + result
    return render_template('result.html', data=result)

# @app.route('/result', methods=['POST'])
# def result(result):
#     result_thrrow = result
#     return render_template('result.html', data = result_thrrow)

if __name__ == '__main__':
    app.run(debug=True)
