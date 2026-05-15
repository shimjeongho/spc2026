import requests

url = 'https://api.github.com/search/repositories'

keyword = "python"

params = {
    'q': keyword,
    'per_page': 100,
    'page': 2
}

resp = requests.get(url, params)
data = resp.json()

# print(data)

if 'items' in data:
    repos = data['items']
    for repo in repos:
        name = repo['name']
        full_name = repo['full_name']
        html_url = repo['html_url']
        desc = repo['description']
        
        print(f'리포명: {name}, 풀네임: {full_name}, URL: {html_url}, 설명: {desc}')

"""
리포명: Python, 풀네임: TheAlgorithms/Python, URL: https://github.com/TheAlgorithms/Python, 설명: All Algorithms implemented in Python
리포명: Python, 풀네임: geekcomputers/Python, URL: https://github.com/geekcomputers/Python, 설명: My Python Examples
리포명: Python, 풀네임: walter201230/Python, URL: https://github.com/walter201230/Python, 설명: 小白 python 教程
리포명: Python, 풀네임: injetlee/Python, URL: https://github.com/injetlee/Python, 설명: Python脚本。模拟登录知乎， 爬虫，操作excel，微信公众号，远程开机
리포명: python, 풀네임: kubernetes-client/python, URL: https://github.com/kubernetes-client/python, 설명: Official Python client library for kubernetes
리포명: python, 풀네임: Show-Me-the-Code/python, URL: https://github.com/Show-Me-the-Code/python, 설명: Show Me the Code Python version.
리포명: Python, 풀네임: gxcuizy/Python, URL: https://github.com/gxcuizy/Python, 설명: Python3编写的各种大小程序，包含从零学Python系列、12306抢票、省市区地址库以及系列网站爬虫等学习源码
리포명: python, 풀네임: flypythoncom/python, URL: https://github.com/flypythoncom/python, 설명: python is all you need !
리포명: python, 풀네임: exercism/python, URL: https://github.com/exercism/python, 설명: Exercism exercises in Python.
리포명: Python, 풀네임: joeyajames/Python, URL: https://github.com/joeyajames/Python, 설명: Python code for YouTube videos.
리포명: python, 풀네임: docker-library/python, URL: https://github.com/docker-library/python, 설명: Docker Official Image packaging for Python
리포명: PythonDataScienceHandbook, 풀네임: jakevdp/PythonDataScienceHandbook, URL: https://github.com/jakevdp/PythonDataScienceHandbook, 설명: Python Data Science Handbook: full text in Jupyter Notebooks
리포명: Python, 풀네임: Tanu-N-Prabhu/Python, URL: https://github.com/Tanu-N-Prabhu/Python, 설명: This repository helps you learn Python and Machine Learning from scratch.
리포명: PythonRobotics, 풀네임: AtsushiSakai/PythonRobotics, URL: https://github.com/AtsushiSakai/PythonRobotics, 설명: Python sample codes and textbook for robotics algorithms.
리포명: awesome-python, 풀네임: vinta/awesome-python, URL: https://github.com/vinta/awesome-python, 설명: An opinionated list of Python frameworks, libraries, tools, and resources
리포명: Python-100-Days, 풀네임: jackfrued/Python-100-Days, URL: https://github.com/jackfrued/Python-100-Days, 설명: Python - 100天从新手到大师
리포명: Complete-Python-3-Bootcamp, 풀네임: Pierian-Data/Complete-Python-3-Bootcamp, URL: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp, 설명: Course Files for Complete Python 3 Bootcamp Course on Udemy
리포명: python, 풀네임: 521xueweihan/python, URL: https://github.com/521xueweihan/python, 설명: 《笨方法学 Python》（Learn Python the Hard Way）学习笔记
리포명: python, 풀네임: poise/python, URL: https://github.com/poise/python, 설명: THIS COOKBOOK IS DEPRECATED – Chef cookbook to install Python and related tools
리포명: learn_python3_spider, 풀네임: wistbean/learn_python3_spider, URL: https://github.com/wistbean/learn_python3_spider, 설명: python爬虫教程系列、从0到1学习python爬虫，包括浏览器抓包，手机APP抓包，如 fiddler、mitmproxy，各种爬虫涉及的模块的使用，如：requests、beautifulSoup、selenium、appium、scrapy等，以及IP代理，验证码识别，Mysql，MongoDB数据库的python使用，多线程多进程爬虫的使用，css 爬虫加密逆向破解，JS爬虫逆向，分布式爬虫，爬虫项目实战实例等
리포명: learn-python3, 풀네임: michaelliao/learn-python3, URL: https://github.com/michaelliao/learn-python3, 설명: Learn Python 3 Sample Code
리포명: python3-cookbook, 풀네임: yidao620c/python3-cookbook, URL: https://github.com/yidao620c/python3-cookbook, 설명: 《Python Cookbook》 3rd Edition Translation
리포명: Python, 풀네임: Yonv1943/Python, URL: https://github.com/Yonv1943/Python, 설명: Demo and other Python3 code
리포명: python, 풀네임: meshtastic/python, URL: https://github.com/meshtastic/python, 설명: The Python CLI and API for talking to Meshtastic devices
리포명: PythonPark, 풀네임: Jack-Cherish/PythonPark, URL: https://github.com/Jack-Cherish/PythonPark, 설명: Python 开源项目之「自学编程之路」，保姆级教程：AI实验室、宝藏视频、数据结构、学习指南、机器学习实战、深度学习实战、网络爬虫、大厂面经、程序人生、资源分享。
리포명: python-patterns, 풀네임: faif/python-patterns, URL: https://github.com/faif/python-patterns, 설명: A collection of design patterns/idioms in Python
리포명: python-cheatsheet, 풀네임: gto76/python-cheatsheet, URL: https://github.com/gto76/python-cheatsheet, 설명: Comprehensive Python Cheatsheet
리포명: PythonSpiderNotes, 풀네임: lining0806/PythonSpiderNotes, URL: https://github.com/lining0806/PythonSpiderNotes, 설명: Python入门网络爬虫之精华版
리포명: python, 풀네임: zhanghe06/python, URL: https://github.com/zhanghe06/python, 설명: Python使用记录
리포명: python-guide, 풀네임: realpython/python-guide, URL: https://github.com/realpython/python-guide, 설명: Python best practices guidebook, written for humans. 
"""