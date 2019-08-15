import subprocess


def client_run():
    process= subprocess.Popen(['fab client:r'], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    code = process.communicate()
    print (code[0].decode('utf-8'))



client_run()
