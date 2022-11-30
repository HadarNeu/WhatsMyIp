from subprocess import check_output

def local_ipv4():
    internalIP = check_output(['hostname', '-I'])
    internalIP = str(internalIP)[2:-3]
    return internalIP

print(local_ipv4(), type(local_ipv4()))
