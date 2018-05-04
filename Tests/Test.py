from API.apicalls import Requests
from API.parser import Parser


# import API.data
# import API.codedecode


def main():
    call = Requests()
    print(call.post_login(user='jay@mailinator.com', password='123456').text)


if __name__ == '__main__':
    main()
