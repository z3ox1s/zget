try:
    from colorama import Fore
    from requests import get

except:
    print(f'\n[{Fore.RED}-{Fore.WHITE}] An error has occurred in requirements calling')

else:
    # Split function
    def split(txt, seps): # Split function
            default_sep = seps[0]

            for sep in seps[1:]:
                txt = txt.replace(sep, default_sep)
            return [i.strip() for i in txt.split(default_sep)]

    # Main function
    def getMethod(target, payloadF = '', payloadH = '', payloadC = '', payloadU = '', payloadRH = '', filename = ''):
        payload_F = dict()
        payload_H = dict()
        payload_C = dict()

        if payloadH != None:
            lowerH = payloadH.lower()
        else:
            lowerH = ''

        try:
            plf = split(payload_F, ('=', '&'))
            
            for i in range(0, int(len(plf)), 2):
                payload_F[plf[i]] = plf[i + 1]

        except AttributeError:
            pass

        if payloadH:
            plh = split(payload_H, (':', ','))

            for i in range(0, int(len(plh)), 2):
                payload_H[plh[i]] = plh[i + 1]

        if payloadC:
            plc = split(payload_C, (':', ','))

            for i in range(0, int(len(plc)), 2):
                payload_C[plc[i]] = plc[i + 1]

        if payloadU != '' and 'user-agent' not in lowerH:
            payload_H['User-Agent'] = payloadU

        if filename:
            print(f'\n[{Fore.YELLOW}!{Fore.WHITE}] Trying to download the file, please wait...')

            try:
                resp = get(target)

                with open(filename, 'wb') as f:
                    f.write(resp.content)

                print(f'\n[{Fore.GREEN}+{Fore.WHITE}] File downloaded successfully.')

            except:
                print(f'\n[{Fore.RED}-{Fore.WHITE}] An error has occurred during the download.')
        
        else:
            response = get(target, data = payload_F, headers = payload_H, cookies = payload_C, allow_redirects = True)
            
            if payloadRH:
                if response.status_code == 404:
                    print(f'\n[{Fore.RED}-{Fore.WHITE}] Page {Fore.RED}{target} {Fore.WHITE}seems not exist.')
                
                else:
                    print(f'\n{Fore.GREEN}Response:{Fore.WHITE}\n', response.text, f'\n{Fore.YELLOW}Headers:{Fore.WHITE}\n', response.headers)

            else:
                if response.status_code == 404:
                    print(f'\n[{Fore.RED}-{Fore.WHITE}] Page {Fore.RED}{target} {Fore.WHITE}seems not exist.')
                
                else:
                    print(f'\n{Fore.GREEN}Response:{Fore.WHITE}\n' + response.text)
