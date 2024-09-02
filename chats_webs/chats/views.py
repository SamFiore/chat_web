from django.shortcuts import render,redirect
# from django.http import JsonResponse
from django.contrib.auth import get_user
import json
# Create your views here.
def sala_chats(req):
    if req.method == 'POST':
        with open('chats/logs/id_count.txt','r') as file:
            dataNum = file.read()
            dataNum = int(dataNum)
            dataNum += 1
        user = get_user(req)
        msg = {dataNum:[str(user),req.POST.get("barra_chat",default=None)]}
        with open('chats/logs/id_count.txt','w') as file:
            file.write(str(dataNum))
            file.close()
        with open('chats/logs/json_logs.JSON','r') as file:
            data = json.load(file)
        data["log"].append(msg)
        with open('chats/logs/json_logs.JSON','w') as file:
            json.dump(data,file)
        return redirect('salas')
    with open('chats/logs/json_logs.JSON','r') as file:
        dict_with_logs = {}
        data = json.load(file)
        for user_log in data['log']:
            user_log = dict(user_log)
            xid, xcontent = next(iter(user_log.items()))
            dict_with_logs[xid] = xcontent
    return render(req,'salas/plantilla_sala.html',{'dict_with_logs':dict_with_logs})
