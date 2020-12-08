import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    page = requests.get("https://youlead.id/")
    soup = BeautifulSoup(page.content, 'html.parser')
    wProgramSubTitle = soup.select(".program_sub_title")
    wProgramDesc = soup.find_all(class_="program_desc")

    lProgramSubTitle = [
        item.get_text().strip('\n').strip()
        for item in wProgramSubTitle
    ]
    lProgramDesc = [
        item.get_text().strip().strip('\n')
        for item in wProgramDesc
    ]

    i = 0
    j = 0
    result = []
    for x in lProgramSubTitle:
        for y in lProgramDesc:
            if(i == j):
                # print(adj[i], fruits[j])
                data = {
                    "programDesc": lProgramSubTitle[i],
                    "programSubTitle": lProgramDesc[j],
                }

                result.append(data)
            else:
                continue
            j = j + 1
        i = i + 1

    return jsonify(result)

app.run(debug=True, host='localhost', port= 8000)