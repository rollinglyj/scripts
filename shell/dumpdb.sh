
monitorTables=(mon_dag_edge mon_data mon_data_instance mon_flow mon_flow_instance mon_monitor mon_monitor_instance
               mon_monitor_user_admin mon_monitor_user_subscribe mon_monitor_version )

for table in ${monitorTables[@]}
do
   ./mysqldump -h127.0.0.1 -P3300 -u udw -pudw --default-character-set=utf8 udw $table   > ./$table.sql    
done




