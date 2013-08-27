import os
import MailClient

data = ['nova_ad_display','36237.41', '9996.51%', '36237.53', '6.51%' ,'8865.61','0.48%','782.96', '37.75%','46.28', '0.24', '1.00','<font color="green" size="5">8888</font>','<font color="green" size="5">8888</font>','<font color="#FF0000" size="5">8888</font>']

if __name__=='__main__':
    mailclient       = MailClient.MailClient()
    i                = 0
    #for i in range(100):
    if True:
        content_list = ['QE-31'+str(i), 'xuekang',  'xuekang',  'major',  'resolved',  '2013070313',  '2013070313', 'online'  ]
        title        = '[UDW Statistic] The Efficient Bill of UAP mission 2013-08-27'
        from_email   = 'chenzefeng@baidu.com'
        to_email     = 'chenzefeng@baidu.com'
        template_id  = '24'
        mailclient.sendBanch(from_email, to_email,title,data,"list",template_id)
        mailclient.sendBanch(from_email, to_email,title,data,"list",template_id)
        mailclient.sendBanch(from_email, to_email,title,data,"list",template_id)
        
    
    
    
