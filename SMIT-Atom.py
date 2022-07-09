#  [*] Programmer Mmdrza.Com [*]Telegram Channel:@mPython3  [*]Programmer iD @PyMmdrza

import blocksmith
import pandas as pd
import random
import requests
import multiprocessing
from multiprocessing import Pool, Process, cpu_count
from colorama import Fore, Style
from rich.console import Console
from lxml import html

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


def Bal(address):
    urlblock = "https://bitcoin.atomicwallet.io/address/" + address
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


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
        urlblock = "https://bitcoin.atomicwallet.io/address/" + addr
        respone_block = requests.get(urlblock)
        byte_string = respone_block.content
        source_code = html.fromstring(byte_string)
        xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
        treetxid = source_code.xpath(xpatch_txid)
        xVol = str(treetxid[0].text_content())
        bal = str(xVol)
        ifer = '0 BTC'
        sert += 1

        if str(bal) != str(ifer):
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
