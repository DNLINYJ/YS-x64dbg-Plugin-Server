from flask import Flask,request
import json
app = Flask(__name__)
 
@app.route('/jmp_address',methods=['POST'])
def test():
    # {"offset":jmp指令的偏移量, "jmp_offset":jmp指令跳转的地址偏移量}
    temp_json = json.loads(request.data.decode('utf-8'))
    offset = temp_json['offset']
    jmp_offset = temp_json['jmp_offset']
    with open("offset_jmp_already.json","r",encoding="utf-8") as f:
        json_old = json.load(f) 
    json_old[offset] = jmp_offset
    with open("offset_jmp_already.json","w",encoding="utf-8") as f:
        json.dump(json_old, f)
    return "OK"
if __name__ == '__main__':
    app.run(port=50000)