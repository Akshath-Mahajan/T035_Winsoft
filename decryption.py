import numpy as np
encrypted_string = "Cnwvtus KuaiTaa rlodeeurethn  an Ia_mrhs baer oag ndC_a aeoat dLj lLdio_me  p  hagZLngan _"
key = "DELHI"
def remove_double_space(string):
    temp = string.split(' ')
    temp = [i for i in temp if i]
    return ' '.join(temp)
def decrypt(enc, key):
    temp_key = sorted(key.upper())
    cols = len(temp_key)
    rows = len(enc)//cols
    arr = [[None for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = enc[j*rows + i]
    _map = {}
    arr = np.array(arr)
    for i in range(cols):
        _map[temp_key[i]] = arr[:,i]
    arr = []
    for i in range(cols):
        arr.append(_map[key[i]])
    arr = np.array(arr).T
    arr = arr.flatten()
    return remove_double_space(''.join(arr).rstrip('_'))

a = decrypt(encrypted_string, key)
print(a)