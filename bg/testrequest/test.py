import  requests
#查询天气预报接口
url ="http://apis.juhe.cn/simpleWeather/query"
r=requests.get(url,params={"city":"温州"})
result=r.json()