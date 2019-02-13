"""
restapi.py
Mihaela
February 9, 2019

Python requests documentation: http://docs.python-requests.org/en/master/
"""
import requests


def fetch(url, fout):
    """
    Fetches response from GET with url and saves text content of response in
        fout file.
    Parameters:
        url: string
        fout: file object opened for writing
    Returns:
        integer
    """
    r = requests.get(url)
    fout.write(r.text)
    fout.close()
    return r.status_code


def do_fetch():
    """
    Creates 'fetched_content.txt' file and calls fetch() with url obtained
        from the user and fout pointing to the the text file.
        Prints out status code.
    """
    fout = open('fetched_content.txt', 'w')
    fout.write(f'========== fetched_content.txt ==============\n')
    url = input('--> Enter URL: ')
    status = fetch(url, fout)
    fout.close()
    print(
        f'status code: {status}.\n'
        f'response content fom GET "fetched_content.txt"'
    )


def fetch_details(url, fout):
    """
    Fetches response from GET with url and appends details in fout file.
    Parameters:
        url: string
        fout: file object opened for appending
    """
    r = requests.get(url)
    fout.write(f'url: {r.url}\n')
    fout.write(f'status: {r.status_code}\n')
    fout.write(f'headers:  {r.headers}\n')
    if len(r.text) > 1040:
        fout.write(
            f'content snippet (1000 - 1040 byte range): '
            '{r.text[1000:1040]}\n'
        )
    fout.close


def do_fetch_details():
    """
    Creates 'fetched_details.txt' file and calls fetch_details() with url
        obtained and fout pointing to the text file.
    """
    fout = open('fetched_details.txt', 'a')
    fout.write(f'========== fetched_details.txt ==============\n')
    url = input('--> Enter URL: ')
    fetch_details(url, fout)
    fout.close
    print('response details from GET  in "sent_content.txt"')


def send(form_data, fout):
    """
    Fetches response POST to form_data to https://httpbin.org/post and saves
        text content of response in fout
    Parameters:
        form_data: dictionary
        fout: file object opened for writing
    """
    r = requests.post('https://httpbin.org/post', data=form_data)
    fout.write(r.text)


def do_send():
    """
    Creates 'sent_content.txt' file and calls send() with form values obtained
        from the user and fout ointint to the text file.
    """
    fout = open('sent_content.txt', 'w')
    fout.write(f'========== sent_content.txt ==============\n')
    value1 = input('--> Enter value for key 1: ')
    value2 = input('--> Enter value for key 2: ')
    value3 = input('--> Enter value for key 3: ')
    form_data = {'key1': value1, 'key2': value2, 'key3': value3}
    send(form_data, fout)
    fout.close()
    print('response content from POST in "sent_content.txt"')


if __name__ == '__main__':
    print("running do_fetch")
    do_fetch()

    #print("running do_fetch_details")
    #do_fetch_details()

    #print("running do_send")
    #do_send()
