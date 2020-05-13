import yfinance as yf

import xlsxwriter

import PySimpleGUI as sg

"""
Program to output data about a stock
"""


def main():
    layout = [
        [sg.Text('Stock Research')],
        [sg.Text('Enter stock symbol'), sg.InputText()],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    window = sg.Window('Stock Research', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        elif event == 'Ok':
            i = stockInfo(values[0])
            saveInfo(i, values[1])
    window.close()


def stockInfo(symbol):

    s = yf.Ticker(symbol)
    name = s.info['shortName']
    return(name)


def saveInfo(info, path):
    filepath = path + '/' + info
    with open(filepath, 'w') as f:
        f.write(info)

    sg.popup(f'Stock info for {info} saved to {filepath} ')


main()
