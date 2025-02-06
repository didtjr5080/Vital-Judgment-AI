from ollama import chat
import papago



def ollama_result(vital_sign):
    stream = chat(
        model='llama3',
        messages=[{'role': 'user', 'content': vital_sign}],
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
    return result_trans
    # print(result_trans, end='', flush=True)


