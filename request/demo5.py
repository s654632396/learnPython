# coding=utf-8 

#Event Hooks
import requests

def get_key_info(response, *args, **kwargs):
    """
    callback function
    :param response: 
    :param args: 
    :param kwargs: 
    :return: 
    """
    print response.headers['Content-Type']

def main():
    """
    主程序
    :return: 
    """
    requests.get('https://api.github.com', hooks=dict(response=get_key_info))



if __name__ == '__main__':
    main()