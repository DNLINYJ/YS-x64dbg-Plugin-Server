from flask import Flask,request
import json
app = Flask(__name__)

def ee():
    with open("offset_jmp_already.json","w",encoding="utf-8") as f:
        f.write("[]")
 
ee()

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

@app.route('/jmp_offset_file_path',methods=['GET'])
def file_path():
    ee()
    default_path = "D:\\jmp_files\\offset_jmp_2.json"
    return default_path
    
if __name__ == '__main__':
    app.run(port=50000)
