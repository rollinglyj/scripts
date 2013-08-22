#!/usr/bin/env python
import urllib
import httplib

class MailClient:
    
    '''Send single-line message to server.
        to_email must not null;
        content_kv type is string;
    '''
    def send(self,from_email,to_email,title,warning_message):
        if to_email=='' or to_email==None:
            return;
           
        if not to_email.endswith('@baidu.com'):
            return;
        if warning_message==None or warning_message=='':
            return
        params=urllib.urlencode({'to_email':to_email,'from_email':from_email,'title':title,'content_kv':warning_message,'template_id':'1','client_type':'string'})
        print params;
        conn = httplib.HTTPConnection("cq01-testing-dt23.vm.baidu.com:8080")
        conn.request("GET", "/mailserver/receiver",params)
        r1 = conn.getresponse()
        status= r1.status
        conn.close()
        return status
    
    
    '''
    client_type=['dict','list','derectsend']
    '''
    def sendBanch(self,from_email, to_email,title,content,client_type,template_id='1'):
        if client_type=='derectsend':
            self.send(from_email, to_email,title,content)
        elif client_type=='dict':
            self.sendBanchDict(from_email, to_email, title, content, template_id)
        elif client_type=='list':
            self.sendBanchList(from_email, to_email, title, content, template_id);
    
    '''Send template-packaged message to server.
        to_email: must not null;
        content_kv: a dict, contains the key and its corresponding value;
        template_id: default template id is -1, 
    '''
    def sendBanchDict(self,from_email, to_email,title,content_kv,template_id='1'):
        if to_email=='' or to_email==None:
            return;
           
        if not to_email.endswith('@baidu.com'):
            return;
        if content_kv==None or content_kv=='':
            return
        serialize =''
        for k,v in content_kv.items():
            serialize+=k+'\01'+v+'\02'
        if len(serialize)>=1:
            serialize=serialize[0:-1]               
        params=urllib.urlencode({'to_email':to_email,'from_email':from_email,'title':title,'content_kv':serialize,'template_id':template_id,'client_type':'dict'})
        print params;
        conn = httplib.HTTPConnection("cq01-testing-dt23.vm.baidu.com:8080")
        conn.request("GET", "/mailserver/receiver",params)
        r1 = conn.getresponse()
        status= r1.status
        conn.close()
        return status
    
    def sendBanchList(self,from_email, to_email,title,content_list,template_id='1'):
        if to_email=='' or to_email==None:
            return;
           
        if not to_email.endswith('@baidu.com'):
            return;
        if content_list==None or len(content_list)==0:
            return
        serialize =''
        for k in content_list:
            serialize+=k+'\01'
        if len(serialize)>=1:
            serialize=serialize[0:-1]
        params=urllib.urlencode({'to_email':to_email,'from_email':from_email,'title':title,'content_list':serialize,'template_id':template_id,'client_type':'list'})
        conn = httplib.HTTPConnection("cq01-testing-dt23.vm.baidu.com:8080")
        conn.request("GET", "/mailserver/receiver",params)
        r1 = conn.getresponse()
        status= r1.status
        conn.close()
        return status