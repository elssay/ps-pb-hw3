def get_absolute_url(url, *args, **kwargs):
    
    print(url, end = '/')
    for i in args:
        print(i, end = '/')
       
    
    print(end = '?')
    for k, v in kwargs.items():
        print(f'{k}={v}', end = '&')
    

get_absolute_url('www.yandex.ru', 'posts', 'news', id=24, author='admin')
