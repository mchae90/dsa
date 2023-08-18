import re

def findMatch(self,s):
    #'/api[/\w]*/users/\d+[/\w+_]*[/\w]*'
    ns = re.sub('/users/\d+','/users/{userid}',s)
    print(ns)

    p = '[/\w]+/[\w]*[{\w+}]*[/\w+_]*\w+'

    # p = '[/\w]+/[\w\d]*[/\w+_]*\w+'
    #
    # a = re.findall(p,ns)
    # print(a)
    for m in re.finditer(p, ns):
        print(str(m.start())+str(m.end()))


    # b = re.split(p,ns)
    # mm = collections.defaultdict(str)
    #
    #
    #
    # for k,v in zip(a,b):
    #     mm[k]+=(' ' + v)
    # res = []
    # for i in mm.values():
        # res = re.findall('dyno=web.\d+',i)
        # print(res)
        # for x in res:
        #     print(re.findall('\d+',x))
        # res2 = re.findall('connect=\d+ms',i)
        # # print(res2)
        # for x in res2:
        #     temp = re.findall('\d+',x)
        #     t2 = 0
        #     t2 += sum([int(k) for k in temp])
        #     res.append(t2)

    # print(res)

count the number of times each endpoint is called, 
the average connect time,
and the max dyno of each endpoint (dyno refers to the API The server being called, 
max dyno means which server has been called the most times)
        
#from Solution import Solution
from Solution import Solution
# obj = Solution()
# ret = obj
# print (ret)
# map = {"anna": 2,"matt" :1,"kevin": 5}
a = ['A','B','C','D','E']
b = [100,150,200,500,600]
map = dict(zip(a,b))
obj = Solution()
urls = '2014-01-09T06:16:53.748849+00:00 heroku[router]: at=info method=POST path=/api/online/platforms/facebook_canvas/users/100002266342173/add_ticket host=mygame.heroku.com fwd="94.66.255.106" dyno=web.12 connect=12ms service=21ms status=200 bytes=782014-01-09T06:16:53.742892+00:00 heroku[router]: at=info method=GET path=/api/users/100002266342173/count_pending_messages host=mygame.heroku.com fwd="94.66.255.106" dyno=web.8 connect=9ms service=9ms status=304 bytes=02014-01-09T06:16:53.766841+00:00 heroku[router]: at=info method=POST path=/logs/save_personal_data host=mygame.heroku.com fwd="5.13.87.91" dyno=web.10 connect=1ms service=42ms status=200 bytes=162014-01-09T06:16:53.772938+00:00 heroku[router]: at=info method=POST path=/api/users/100002844291023 host=mygame.heroku.com fwd="46.195.178.244" dyno=web.6 connect=2ms service=43ms status=200 bytes=522014-01-09T06:16:53.765430+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_progress host=mygame.heroku.com fwd="5.13.87.91" dyno=web.11 connect=1ms service=47ms status=200 bytes=74982014-01-09T06:16:53.760472+00:00 heroku[router]: at=info method=POST path=/api/users/1770684197 host=mygame.heroku.com fwd="74.139.217.81" dyno=web.5 connect=1ms service=17ms status=200 bytes=6812014-01-09T06:15:15.893505+00:00 heroku[router]: at=info method=GET path=/api/users/1686318645/get_friends_progress host=mygame.heroku.com fwd="1.125.42.139" dyno=web.3 connect=8ms service=90ms status=‍‌‌‍‌‍‌‌‌‌‍‍‌‌‍‍‌‌‌200 bytes=75342014-01-09T06:16:53.768188+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_score host=mygame.heroku.com fwd="5.13.87.91" dyno=web.13 connect=2ms service=46ms status=200 bytes=75342014-01-09T06:16:53.768188+00:00 heroku[router]: at=info method=GET path=/api/users/100005936523817/get_friends_score'
# ret = obj.findMatch(urls)