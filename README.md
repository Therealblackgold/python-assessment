# python-assessment
  The project was built using the latest Python 3.9.7 version

     Command Line 
    -customUser
     mysql> show databases;
     
      # select db
     mysql> use python_assessment;
     
     # show all tables
     mysql> show tables;
     
     # show all users
     mysql> Select * from accounts_customuser
     
     # export users to excel
     mysql> Select * from table_name into outfile  "path\\to\\excel\\document\\file_name.csv" fields terminated by ', '  lines terminated by '\n '; 

    -tasks
      mysql> show databases;
      mysql> use python_assessment;
      
      # show all tasks
      mysql> select * from tasks_task;
      
      # update task
      UPDATE tasks_task SET title = 'gym at 05:30' WHERE id = 2;
      
      # delete task
      mysql> DELETE FROM tasks_task  WHERE id = 14;
      
      # show complete tasks
      mysql> SELECT complete FROM tasks_task WHERE true;
      
      # show deleted tasks
      mysql> SELECT delete FROM tasks_task WHERE true;
      
      
    

