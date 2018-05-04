from API.apicalls import Requests
from API.parser import Parser


# import API.data
# import API.codedecode


def main():
    call = Requests()
    print(call.get_dashboard().text)


if __name__ == '__main__':
    main()
