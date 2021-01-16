#!/usr/bin/python3

# Requirements
try:
    import argparse
    from requests import get, post, ConnectionError
    from colorama import Fore
    from ssl import SSLCertVerificationError
    from sys import argv

except:
    print(f'\n[{Fore.RED}-{Fore.WHITE}] An error has occurred in requirements calling')

else:
    # Arguments
    parser = argparse.ArgumentParser(usage = 'zget -h', add_help = False)
    parser.add_argument('-h', '--help', action = 'store_true')
    parser.add_argument('-t', '--target')
    parser.add_argument('-G', '--get', action = 'store_true')
    parser.add_argument('-P', '--post', action = 'store_true')
    parser.add_argument('-d', '--data')
    parser.add_argument('-H', '--headers')
    parser.add_argument('-c', '--cookies')
    args = parser.parse_args()

    # Functions
    def main(): # Main function
        if args.get == False and args.post == False:
            getMethod(args.target, args.data, args.headers, args.cookies)

        else:
            if args.get:
                getMethod(args.target, args.data, args.headers, args.cookies)

            elif args.post:
                postMethod(args.target, args.data, args.headers, args.cookies)

    def cmdHelp(): # Help Command
        return '''
Examples:
 
 GET:
  zget -t example.com -G (GET Method)
  zget -t example.com -G -d 'name=value&name=value' (GET + Data)
  zget -t example.com -G -H 'name:value,name:value' (GET + Headers)
  zget -t example.com -G -c 'name:value,name:value' (GET + Cookies)

 POST:
  zget -t example.com -P (POST Method)
  zget -t example.com -P -d 'name=value&name=value' (POST + Data)
  zget -t example.com -P -H 'name:value,name:value' (POST + Headers)
  zget -t example.com -P -c 'name:value,name:value' (POST + Cookies)

Help:
 
 -h, --help                         Help command.
 -t URL, --target URL               Address of target.
 -G, --get                          GET Method.
 -P, --post                         POST Method.
 -d DATA, --data DATA               Data to send to target.
 -H HEADERS, --headers HEADERS      Custom headers to target.
 -c COOKIES, --cookies COOKIES      Cookies to send to target.'''

    def split(txt, seps): # Split function
        default_sep = seps[0]

        for sep in seps[1:]:
            txt = txt.replace(sep, default_sep)
        return [i.strip() for i in txt.split(default_sep)]

    def getMethod(target, data = '', payloadH = '', payloadC = ''): # Get method
        payloadH = dict()
        payloadC = dict()

        if args.headers != None:
            lowerH = args.headers.lower()
        else:
            lowerH = ''

        if args.headers:
            plh = split(args.headers, (':', ','))

            for i in range(0, int(len(plh)), 2):
                payloadH[plh[i]] = plh[i + 1]

        if args.cookies:
            plc = split(args.cookies, (':', ','))

            for i in range(0, int(len(plc)), 2):
                payloadC[plc[i]] = plc[i + 1]

        if 'user-agent' not in lowerH:
            payloadH['User-Agent'] = 'zget/0.0.1'

        response = get(target, data = data, headers = payloadH, cookies = payloadC, allow_redirects = True)
        
        if response.status_code == 404:
            print(f'\n[{Fore.RED}-{Fore.WHITE}] Page {Fore.RED}{target} {Fore.WHITE}seems not exist.')
        
        else:
            print('\n' + response.text)

    def postMethod(target, payloadF = '', payloadH = '', payloadC = ''): # Post method
        payloadF = dict()
        payloadH = dict()
        payloadC = dict()

        if args.headers != None:
            lowerH = args.headers.lower()
        else:
            lowerH = ''

        try:
            plf = split(args.data, ('=', '&'))
            
            for i in range(0, int(len(plf)), 2):
                payloadF[plf[i]] = plf[i + 1]

        except AttributeError:
            pass

        if args.headers:
            plh = split(args.headers, (':', ','))

            for i in range(0, int(len(plh)), 2):
                payloadH[plh[i]] = plh[i + 1]

        if args.cookies:
            plc = split(args.cookies, (':', ','))

            for i in range(0, int(len(plc)), 2):
                payloadC[plc[i]] = plc[i + 1]

        if 'user-agent' not in lowerH:
            payloadH['User-Agent'] = 'zget/0.0.1'

        response = post(target, data = payloadF, headers = payloadH, allow_redirects = True)

        if response.status_code == 404:
            print(f'\n[{Fore.RED}-{Fore.WHITE}] Page {Fore.RED}{target} {Fore.WHITE}seems not exist.')
        
        else:
            print('\n' + response.text)

    # Main
    try:
        print(f'''                       
                             {Fore.MAGENTA})  
             {Fore.MAGENTA}(  (     (   ( /(  
         {Fore.RED}(   )\))(   ))\  )\()) 
         {Fore.RED})\ ((_))\  /((_)(_))/  
        {Fore.RED}((_) (()(_)(_))  | |_   
        {Fore.YELLOW}|_ // _` | / -_) |  _|  
        {Fore.YELLOW}/__|\__, | \___|  \__|  
            {Fore.YELLOW}|___/
                
               {Fore.BLUE}by z3ox1s
                {Fore.GREEN} 0.0.1{Fore.WHITE}''')

        if args.help:
            print(cmdHelp())
        
        else:
            if args.target:
                if '://' not in args.target:
                    args.target = 'http://' + args.target

            if len(argv) == 1:
                print(f"\n[{Fore.RED}-{Fore.WHITE}] Usage: zget -t example.com [OPTIONS] {Fore.RED}or{Fore.WHITE} zget -h to see all parameters.")
            
            else:
                main()

    # Excepts
    except KeyboardInterrupt:
        print(f'\n[{Fore.RED}-{Fore.WHITE}] Action cancelled by user.')

    except ConnectionError:
        print(f'\n[{Fore.RED}-{Fore.WHITE}] An error has occurred during connection to {Fore.RED}{args.target}{Fore.WHITE}')

    except SSLCertVerificationError:
        print(f'\n[{Fore.RED}-{Fore.WHITE}] An error has occurred during the SSL Verification.')

    except:
        print(f"\n[{Fore.RED}-{Fore.WHITE}] Usage: zget -t example.com [OPTIONS] {Fore.RED}or{Fore.WHITE} zget -h to see all parameters.")