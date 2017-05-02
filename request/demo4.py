# coding=utf-8 
# image response
import requests


def download_images():
    """
    demo 下载文件
    :return: 
    """
    url = "http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
    response = requests.get(url, stream=True)
    with open('./demo.png', 'wb') as fh:
        for chunk in response.iter_content(128):
            fh.write(chunk)

def download_image_improved():
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=" \
          "1493488656602&di=0dbc6e8266f8e0cd3da1590075e84e31&imgtype=0&src=http%3A%2F%2F" \
          "www.005.tv%2Fuploads%2Fallimg%2F160708%2F22-160FQ123521b.jpg"
    # response = requests.get(url, stream=True)
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as response:
        with open('./demo1.jpg', 'wb') as fh:
            for chunk in response.iter_content(128):
                fh.write(chunk)



if __name__ == '__main__':
    download_image_improved()
