# coding: UTF-8
def get_unused_gpu():
    import subprocess
    import re
    check = subprocess.check_output("nvidia-smi --query-gpu=index,temperature.gpu,utilization.gpu,utilization.memory --format=csv", shell=True)
    res = re.split(r'\n', check.decode('utf-8'))[1:-1]
    res_csv = []
    for i in res:
        j = i.replace(' %', '')
        res_csv.append(j.split(','))
    for i in range(0, 8):
        if int(res_csv[i][1]) < 40 and int(res_csv[i][2]) == 0 and int(res_csv[i][3]) == 0:
            return res_csv[i][0]
    print("no gpus are available")
    exit(1)
if __name__ == '__main__':
    print(GetUnusedGpu())
