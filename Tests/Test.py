from API import requests
from API.parser import Parser


# import API.data
# import API.codedecode


def main():
    for i in range(20):
        response = requests.post_add_business_bit()
        print(response)


if __name__ == '__main__':
    main()
