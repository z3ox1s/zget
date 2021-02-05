#!/usr/bin/python3

try:
    import argparse
    from colorama import Fore
    from ssl import SSLCertVerificationError
    from sys import argv
    from modules.getmethod import getMethod
    from modules.postmethod import postMethod

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
    parser.add_argument('-U', '--user-agent')
    parser.add_argument('-RH', '--response-headers', action = 'store_true')
    parser.add_argument('-D', '--download')
    args = parser.parse_args()

    # Main function
    def main():
        if args.get == False and args.post == False:
            getMethod(args.target, args.data, args.headers, args.cookies, args.user_agent, args.response_headers, args.download)

        else:
            if args.get:
                getMethod(args.target, args.data, args.headers, args.cookies, args.user_agent, args.response_headers, args.download)

            elif args.post:
                postMethod(args.target, args.data, args.headers, args.cookies, args.user_agent, args.response_headers, args.download)

    # Help Command
    def cmdHelp():
        return '''
Examples:
 
 GET:
  zget -t example.com -G (GET Method)
  zget -t example.com -G -d 'name=value&name=value' (GET + Data)
  zget -t example.com -G -H 'name:value,name:value' (GET + Headers)
  zget -t example.com -G -c 'name:value,name:value' (GET + Cookies)
  zget -t example.com -G -U 'value' (GET + User-Agent)
  zget -t example.com -G -RH (GET + Response Headers)
  zget -t example.com -G -D output (GET + Download)

 POST:
  zget -t example.com -P (POST Method)
  zget -t example.com -P -d 'name=value&name=value' (POST + Data)
  zget -t example.com -P -H 'name:value,name:value' (POST + Headers)
  zget -t example.com -P -c 'name:value,name:value' (POST + Cookies)
  zget -t example.com -P -U 'value' (POST + User-Agent)
  zget -t example.com -P -RH (POST + Response Headers)
  zget -t example.com -P -D output (POST + Download)

Help:
 
 -h, --help                         Help command.
 -t URL, --target URL               Address of target.
 -G, --get                          GET Method.
 -P, --post                         POST Method.
 -d DATA, --data DATA               Data to send to target.
 -H HEADERS, --headers HEADERS      Custom headers to target.
 -c COOKIES, --cookies COOKIES      Cookies to send to target.
 -U, --user-agent USER-AGENT        Custom user-agent send to target.
 -RH, --response-headers            Retrieve response headers from the target.
 -D, --download OUTPUT              Download file from the target.'''

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
                {Fore.GREEN} 0.0.2{Fore.WHITE}''')

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