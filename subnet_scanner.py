from tkinter import *
import netifaces as ni
import ipaddress
import random
import datetime


address_lst = []
interface_lst = []
netmask_lst = []


def getip(if_name):
    text = ni.ifaddresses(if_name)
    ip = text.get(2)
    return (ip[0].get('addr'))

def getmask (if_name):
    text = ni.ifaddresses(if_name)
    ip = text.get(2)
    return (ip[0].get('netmask'))


###### MAIN PROGRAM #######


def main():
    for x in ni.interfaces():
        interface_lst.append(x)

    for x in interface_lst:
        try:
            address_lst.append(getip(x))
            netmask_lst.append(getmask(x))
        except:
            pass


    address_lst.remove('127.0.0.1')
    address = address_lst[0]


    netmask = max(netmask_lst)
    bits = sum(bin(int(x)).count('1') for x in netmask.split('.'))
    cidr = '/' + str(bits)


    IP_Addr = ipaddress.ip_interface(address + cidr)
    Net_Addr = IP_Addr.network
    pref_len = IP_Addr.with_prefixlen
    Mask = IP_Addr.with_netmask
    wildcard = IP_Addr.hostmask
    broadcast_address = Net_Addr.broadcast_address


    output_network_address = str(Net_Addr).split('/')[0]
    output_broadcast_address = broadcast_address
    output_cidr = pref_len.split('/')[1]
    output_netmask = Mask.split('/')[1]
    output_wilcard = wildcard
    output_first = list(Net_Addr.hosts())[0]
    output_last = list(Net_Addr.hosts())[-1]

    L2SV.set('Your ip address: ' + str(address))
    L3SV.set('Network address: ' + str(output_network_address))
    L4SV.set('Broadcast address: ' + str(output_broadcast_address))
    L5SV.set('CIDR notation : /' + str(output_cidr))
    L6SV.set('Subnet Mask: ' + str(output_netmask))
    L7SV.set('Wildcard Mask: ' + str(output_wilcard))
    L8SV.set('Address range: ' + str(output_first) + ' - ' + str(output_last))
    L9SV.set('Updated last: ' + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))

    print('hello')
    root.after(20000, main)

root = Tk()
root.title("Subnet discovery tool")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

L2SV = StringVar()
L3SV = StringVar()
L4SV = StringVar()
L5SV = StringVar()
L6SV = StringVar()
L7SV = StringVar()
L8SV = StringVar()
L9SV = StringVar()


fontsize = 16
fg_color = '#454545' #c93c3c

L1 = Label(master=root, background='#c93c3c', fg='white', height='4', text='Subnet discovery tool', font=('Insaniburger', 30))
L1.pack(fill=X, side='top')

L2 = Label(master=root, textvariable=L2SV, background='#ffffff', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L2.pack(fill=X, side='top')

L3 = Label(master=root, textvariable=L3SV, background='#f2f2f2', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L3.pack(fill=X, side='top')

L4 = Label(master=root, textvariable=L4SV, background='#ffffff', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L4.pack(fill=X, side='top')

L5 = Label(master=root, textvariable=L5SV, background='#f2f2f2', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L5.pack(fill=X, side='top')

L6 = Label(master=root, textvariable=L6SV, background='#ffffff', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L6.pack(fill=X, side='top')

L7 = Label(master=root, textvariable=L7SV, background='#f2f2f2', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L7.pack(fill=X, side='top')

L8 = Label(master=root, textvariable=L8SV, background='#ffffff', fg=fg_color, height='4', font=('Insaniburger', fontsize))
L8.pack(fill=X, side='top')

L9 = Label(master=root, textvariable=L9SV, background='#f2f2f2', fg=fg_color, height='5', font=('Insaniburger', fontsize))
L9.pack(fill=X, side='top')

L2SV.set('/')
L3SV.set('/')
L4SV.set('/')
L5SV.set('/')
L6SV.set('/')
L7SV.set('/')
L8SV.set('/')
L9SV.set('/')

root.after(20, main)
root.mainloop()


