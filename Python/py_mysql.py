import MySQLdb

try:
   conn_remote = MySQLdb.connect(host='10.216.123.63',user='dc_user',passwd='dc_user',db='SZWG_ECOMON',port=3306)
   #conn_local = MySQLdb.connect(host='10.46.190.21', user='mysql', passwd='mhxzkhl',db='test', port=3306)
   conn_local = MySQLdb.connect(host='localhost', user='mysql', passwd='mhxzkhl',db='test', port=3306)

   cur_remote = conn_remote.cursor()
   cur_local  = conn_local.cursor()
   
#   cur_remote.execute('select * from job_info where user=\'dt-udw-etl\' limit 10')
   cur_remote.execute('select * from job_info where user=\'dt-udw-insight\' limit 10')
   results     = cur_remote.fetchall();
   for row in results:
      for i in row:
         print str(i)+" ",
      print
   values      = []
   for row in results:
      values   = []
      for i in range(18):
         values.append(str(row[i]))
      job_name = str(row[1])
      values.append(job_name[0,job_name.find('_2012')])
      print "values-------------------------------"+str(values)
   cur_local.execute('insert into job_info_new values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',values)
   print "invinsible seperator line-----------------------------------"
   
   cur_local.execute('select * from job_info limit 10')
   results_2   = cur_local.fetchall()
   for row in results_2:
      print row
   conn_local.commit()
   cur_remote.close()
   conn_remote.close()
   cur_local.close()
   conn_local.close()
except MySQLdb.Error,e:
       print "Mysql Error %d: %s" % (e.args[0], e.args[1])

  
