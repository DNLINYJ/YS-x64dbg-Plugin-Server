from flask import Flask,request
import json
app = Flask(__name__)

import difflib
#判断相似度的方法，用到了difflib库
def get_equal_rate_1(str1, str2):
   return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


num = 1

def ee():
    with open("jmp.json","w",encoding="utf-8") as f:
        json.dump({}, f)

def mw():
    with open("mov.json","w",encoding="utf-8") as f:
        json.dump({}, f)

ee()
mw()

@app.route('/jmp_address',methods=['GET'])
def test():
    offset = request.args.get("offset")
    jmp_offset = request.args.get("jmp_offset").replace("%20"," ")
    with open("jmp.json","r",encoding="utf-8") as f:
        a = json.load(f)
    if offset not in list(a.keys()):
        a[offset] = [jmp_offset]
    else:
        a[offset].append(jmp_offset)
    with open("jmp.json","w",encoding="utf-8") as f:
        json.dump(a, f)
    return "OK"

@app.route('/mov_address',methods=['GET'])
def mov_test():
    offset = request.args.get("offset")
    mov_offset = request.args.get("mov_offset").replace("%20"," ")
    with open("mov.json","r",encoding="utf-8") as f:
        a = json.load(f)
    if offset not in list(a.keys()):
        a[offset] = [mov_offset]
    else:
        a[offset].append(mov_offset)
    with open("mov.json","w",encoding="utf-8") as f:
        json.dump(a, f)
    return "OK"

@app.route('/check_jmp_command',methods=['GET'])
def diif():
    c = request.args.get("c")
    return str(get_equal_rate_1(str(c), "jmp rax"))

@app.route('/check_mov_command',methods=['GET'])
def diif_mov():
    c = request.args.get("c")
    return str(get_equal_rate_1(str(c), "mov rax, [rcx+rax*8]"))

if __name__ == '__main__':
    app.run(port=50000)
