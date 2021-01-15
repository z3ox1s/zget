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
    parser = argparse.ArgumentParser(usage = 'zget [OPTIONS]', description = "Ex: zget -t example.com -G -d 'example=example&ex=ex' -H 'Example1: Example1,Example2:Example' -c 'Cookie: EXAMPLE=example'")
    parser.add_argument('-t', '--target', help = 'Address of target')
    parser.add_argument('-G', '--get', action = 'store_true', help = 'GET Method,')
    parser.add_argument('-P', '--post', action = 'store_true', help = 'POST Method,')
    parser.add_argument('-d', '--data', help = 'Data to sent to target.')
    parser.add_argument('-H', '--headers', help = 'Custom headers to target.')
    parser.add_argument('-c', '--cookies', help = 'Cookies to sent to target.')
    args = parser.parse_args()

    # Functions
    def main():
        if args.get:
            getMethod(args.target, args.data, args.headers, args.cookies)

        elif args.post:
            postMethod(args.target, args.data, args.headers, args.cookies)

    def split(txt, seps):
        default_sep = seps[0]

        for sep in seps[1:]:
            txt = txt.replace(sep, default_sep)
        return [i.strip() for i in txt.split(default_sep)]

    def getMethod(target, data = '', payloadH = '', payloadC = ''):
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

    def postMethod(target, payloadF = '', payloadH = '', payloadC = ''):
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

        if 'user-agent' not in lowerH:
            payloadH['User-Agent'] = 'zget/0.0.1'

        response = post(target, data = payloadF, headers = payloadH, allow_redirects = True)

        if response.status_code == 404:
            print(f'\n[{Fore.RED}-{Fore.WHITE}] Page {Fore.RED}{target} {Fore.WHITE}seems not exist.')
        
        else:
            print('\n' + response.text)

    # Main function
    try:
        if args.target:
            if '://' not in args.target:
                args.target = 'http://' + args.target

        print(f'''{Fore.RED}                        
                             )  
             (  (     (   ( /(  
         (   )\))(   ))\  )\()) 
         )\ ((_))\  /((_)(_))/  
        ((_) (()(_)(_))  | |_   
        |_ // _` | / -_) |  _|  
        /__|\__, | \___|  \__|  
            |___/{Fore.WHITE}
                
               {Fore.BLUE}by{Fore.WHITE} {Fore.RED}z3ox1s{Fore.WHITE}
                {Fore.BLUE}v0.0.1{Fore.WHITE}''')

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