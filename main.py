from flask import Flask, render_template, request
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

    # 값 확인 (디버깅)
    print(f"bpmax: {bpmax}, bpmin: {bpmin}, temp: {temp}, pulse: {pulse}, br: {br}")

    # 값이 없을 경우 오류 메시지 출력
    if not all([bpmax, bpmin, temp, pulse, br]):
        return f" 모두 입력해주세요!<br>bpmax={bpmax}, bpmin={bpmin}, temp={temp}, pulse={pulse}, br={br}", 400

    thrrow = f"BP: {bpmax}/{bpmin}, Temperature: {temp}, Pulse: {pulse}, Breath: {br}"
    result = ollama_api.ollama_result(thrrow)
    result = result.replace('\n', '<br>')
    return render_template('result.html', data=result)

# @app.route('/result', methods=['POST'])
# def result(result):
#     result_thrrow = result
#     return render_template('result.html', data = result_thrrow)

if __name__ == '__main__':
    app.run(debug=True)
