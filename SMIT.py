#  [*] For Running This Script Needed Node BTC (BLOCK EXPLORER Exlusive) 
#  [*] Can Insert and Edit Code Checked Balance on Localhost node to ip server node.
#  [*] Programmer Mmdrza.Com [*]Telegram Channel:@mPython3  [*]Programmer iD @PyMmdrza

import blocksmith
import pandas as pd
import random
import requests
import multiprocessing
from multiprocessing import Pool, Process, cpu_count
from colorama import Fore, Style
from rich.console import Console

console = Console()
console.clear()

r = 0

# =========================================================================================
mmdrza = '''
[dark_red]    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗[/]
[red3]    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║[/]
[red1]    ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║[/]
[orange_red1]    ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║[/]
[dark_orange]    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║[/]
[orange1]    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝[/]
'''
# ============================================================================================
console.print(mmdrza)


def seek(r, df_handler):
    global num_threads
    sert = 0
    w = 0
    filename = "btc.txt"
    with open(filename) as f:
        add = f.read().split()
    add = set(add)

    while True:
        paddress_1aphrase = blocksmith.KeyGenerator()
        paddress_1aphrase.seed_input('qwertyuiopasdfghjklzxcvbnm1234567890')  # paddress_1aphrase
        private_Key = paddress_1aphrase.generate_key()
        addr = blocksmith.BitcoinWallet.generate_address(private_Key)
        reqxg = requests.get("http://localhost:5000/balance?active=" + addr).text
        frg = reqxg
        bal = int(frg)
        sert += 1

        if int(bal) > 0:
            w += 1
            with open("WinnerSmit.txt", "a") as fw:
                fw.write('\nADDR: ' + str(addr) + '     BAL:' + str(bal) + '\nKEY: ' + str(
                    private_Key) + '\n------------------------(MMDRZA.COM)---------------------')
                fw.close()

        elif str(addr) in add:
            w += 1
            with open("WinnerSmit.txt", "a") as fx:
                fx.write('\nADDR: ' + str(addr) + '     BAL:' + str(bal) + '\nKEY: ' + str(
                    private_Key) + '\n------------------------(MMDRZA.COM)---------------------')
                fx.close()

        else:
            console.print('[gold1]' + str(sert) + '[/][green] : ' + str(
                addr) + ' : [/][yellow]' + str(
                private_Key) + '[/][green] :  - B:[/][gold1]' + str(bal) + '[/][b green]  W:[/][with]' + str(
                w) + '[/]')


if __name__ == '__main__':
    jobs = []
    df_hanler = pd.read_csv(open("btc.txt", "r"))
    cor = cpu_count()
    cores = int(
        console.input('[white on blue]HOW MANY CORE WANT TO USED: [/][b on red1](Avalible:[gold1]' + str(
            cor) + '[/][white]) [/]'))
    for r in range(cores):
        p = multiprocessing.Process(target=seek, args=(r, df_hanler))
        jobs.append(p)
        p.start()
