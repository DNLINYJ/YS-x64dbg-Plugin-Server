from flask import Flask,request
import json
app = Flask(__name__)
 
@app.route('/jmp_address',methods=['GET'])
def test():
    offset = request.args.get("offset")
    jmp_offset = request.args.get("jmp_offset")
    with open("offset_jmp_already.json","r",encoding="utf-8") as f:
        json_old = json.load(f) 
    json_old.append({offset : jmp_offset})
    with open("offset_jmp_already.json","w",encoding="utf-8") as f:
        json.dump(json_old, f)
    return "OK"
if __name__ == '__main__':
    app.run(port=50000)