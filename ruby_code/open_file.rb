#!/usr/bin/ruby -w
passwd = File.open('./1.data')
puts passwd.fileno

hosts = File.open('./2.data')
puts hosts.fileno
passwd.close

null = File.open('/dev/null')
puts null.fileno
