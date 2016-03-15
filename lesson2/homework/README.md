# Homework task

Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, которая создаёт из этих ключей и значений словарь. Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым не хватило ключей, нужно игнорировать.  

Предположим, у нас есть access.log Apache веб-сервера. Нужно написать функцию, которая найдет десять IP-адресов, от которых было больше всего запросов. Пример формата лога и самого лога можно найти по ссылке: http://ossec-docs.readthedocs.org/en/latest/log_samples/apache/apache.html

Webserver access log sample taken from http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html
text sample
```
slppp6.intermind.net - - [01/Aug/1995:00:00:10 -0400] "GET /history/skylab/skylab.html HTTP/1.0" 200 1687
piweba4y.prodigy.com - - [01/Aug/1995:00:00:10 -0400] "GET /images/launchmedium.gif HTTP/1.0" 200 11853
slppp6.intermind.net - - [01/Aug/1995:00:00:11 -0400] "GET /history/skylab/skylab-small.gif HTTP/1.0" 200 9202
slppp6.intermind.net - - [01/Aug/1995:00:00:12 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
ix-esc-ca2-07.ix.netcom.com - - [01/Aug/1995:00:00:12 -0400] "GET /history/apollo/images/apollo-logo1.gif HTTP/1.0" 200 1173
slppp6.intermind.net - - [01/Aug/1995:00:00:13 -0400] "GET /history/apollo/images/apollo-logo.gif HTTP/1.0" 200 3047
uplherc.upl.com - - [01/Aug/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
133.43.96.45 - - [01/Aug/1995:00:00:16 -0400] "GET /shuttle/missions/sts-69/mission-sts-69.html HTTP/1.0" 200 10566
kgtyk4.kj.yamagata-u.ac.jp - - [01/Aug/1995:00:00:17 -0400] "GET / HTTP/1.0" 200 7280
```

After parsing with logparser.py the result is
```
[('edams.ksc.nasa.gov', 6530), ('piweba4y.prodigy.com', 4846), ('163.206.89.4', 4791), ('piweba5y.prodigy.com', 4607), ('piweba3y.prodigy.com', 4416), ('www-d1.proxy.aol.com', 3889), ('www-b2.proxy.aol.com', 3534), ('www-b3.proxy.aol.com', 3463), ('www-c5.proxy.aol.com', 3423), ('www-b5.proxy.aol.com', 3411)]
```
