import yfinance as yf
import PySimpleGUI as sg

"""
Program to output data about a stock
"""

# To do
# improve GUI wording and look
# close first GUI window after popup
# Add graphs and data to excel
# add buy/sell rating, maybe


def main():
    layout = [
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
            symbol = values[0]
            path = values[1]
            saveInfo(stockInfo(symbol), path)
    window.close()


def stockInfo(symbol):

    s = yf.Ticker(symbol)

    try:
        info = s.info
    except:
        sg.popup('Oops something went wrong.')
        raise SystemExit

    global company
    company = info['shortName']
    sg.popup_ok_cancel(f'Getting information on {company}. Is that correct?')
    return(info)


def saveInfo(data, path):

    filepath = f"{path}/{data['symbol']}"

    with open(filepath, 'w') as f:
        f.write(str(data))

    sg.popup(f'Stock info for {company} saved to {filepath}')


main()
