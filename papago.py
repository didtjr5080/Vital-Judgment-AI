def tranlanor_kor_to_eng(text):
    import urllib.request
    import json  # JSON 응답을 다루기 위해 추가

    from secret_client_key import client_id, client_secret

    content_type = "application/x-www-form-urlencoded"

    encText = urllib.parse.quote(text)  # 번역할 텍스트
    data = "source=ko&target=en&text=" + encText

    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    request.add_header("Content-Type", content_type)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))  # JSON 변환
        translated_text = response_json["message"]["result"]["translatedText"]  # 번역된 문장 추출
        result = translated_text
        # print(translated_text)  # 번역된 문장만 출력
    else:
        result = ("Error Code:", rescode)
        # print("Error Code:", rescode)
    return result

def tranlanor_eng_to_kor(text):
    import urllib.request
    import json  # JSON 응답을 다루기 위해 추가

    from secret_client_key import client_id, client_secret

    content_type = "application/x-www-form-urlencoded"

    encText = urllib.parse.quote(text)  # 번역할 텍스트
    data = "source=en&target=ko&text=" + encText

    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    request.add_header("Content-Type", content_type)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))  # JSON 변환
        translated_text = response_json["message"]["result"]["translatedText"]  # 번역된 문장 추출
        result = translated_text
        # print(translated_text)  # 번역된 문장만 출력
    else:
        result = ("Error Code:", rescode)
        # print("Error Code:", rescode)
    return result