from ollama import chat
import papago

stream = chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'BP: 120/60, temperleture: 36.5, pusle: 14, breath: 15'}],
    stream=True,
)


trans_to_eng = ""
print("----")
for chunk in stream:
    # print(len(chunk['message']['content']))
    print(chunk['message']['content'], end='', flush=True)
    trans_to_eng = trans_to_eng + chunk['message']['content']
    # print("tingking... (", len(trans_to_eng), ")")
print("----")
result_trans = papago.tranlanor_eng_to_kor(trans_to_eng)
print(result_trans, end='', flush=True)


