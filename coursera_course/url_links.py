import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


def get_correct_link(url, position=18):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    link = ''

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        counter += 1
        if counter == position:
            link = tag.get('href', None)
        else:
            continue

    return link


def get_correct_link_n_times(count=7):
    """
    Run the get_correct_link function a specific number of times.
    Each time the correct link is found, we have to rerun the function to find it's correct link.
    So basically -> find correct first link, then find second correct link, then find third correct link
    :param n:
    :return:
    """
    url = 'http://py4e-data.dr-chuck.net/known_by_Sebastien.html'
    result = [url]

    first = get_correct_link(url)
    result.append(first)
    second = get_correct_link(first)
    result.append(second)
    third = get_correct_link(second)
    result.append(third)
    fourth = get_correct_link(third)
    result.append(fourth)
    fifth = get_correct_link(fourth)
    result.append(fifth)
    sixt = get_correct_link(fifth)
    result.append(sixt)
    seventh = get_correct_link(sixt)
    result.append(seventh)

    for n in result:
        print(n)


if __name__ == '__main__':
    get_correct_link_n_times()
