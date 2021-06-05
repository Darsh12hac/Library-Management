from datetime import date
print("---------------------------------------------WELCOME TO THE LIBRARY---------------------------------")
libId=int(input("Enter Login Id:"))
password= input("Enter the Password;")
if password==("s"):
    print("Login Successfully.....")
    print("MAIN MENU:")
    print("1.BOOK INFO \t 2. STUDENT INFO  \t 3. issue  ")
    ch="y"
    while ch=="y":
        a=int(input("Enter ur choice:"))
        ##TO ADD RECORD OF BOOKS #####


       
              
        if (a==1):
             print("-------------------------------------------------------BOOK INFORMATION----------------------------------------------------------------")
             print("MAIN MENU")
             print("1.INSERT \t 2.SEARCH")
             ch="i"
             while ch=="i":
                f=int(input("Enter ur choice:"))
                if (f==1):
                    n=int(input("Enter total no of book u want to insert...."))
                    for i in range(n):
                        def insert_data():
                            import mysql.connector
                            con=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                            cursor=con.cursor()
                            bookid=int(input("Enter book id"))
                            book_name=input("Enter book_name:")
                            publication=input("Enter book public")
                            year=int(input("Enter year:"))
                            qry=("insert into book values(%s,%s,%s,%s)")
                            data=(bookid,book_name,publication,year)
                            cursor.execute(qry,data)
                            con.commit()
                            cursor.close()
                            con.close()                
                            print("Record inserted")

                
                        def Display_rec():
                            import mysql.connector
                            cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                            print("Connection successfully")
                            cursor=cnx.cursor()
                            cursor.execute("select * from book")
                         
                            myrec=cursor.fetchall()
                            for x  in myrec:
                                 print(x)
                            cnx.close()



                        insert_data()
                        Display_rec()     


                if(f==2):
                    def Search_rec():
                        import mysql.connector
                        cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                        print("Connection successfully")
                        cursor=cnx.cursor()
                        search=int(input("Enter the id......."))
                        cursor.execute("select * from book where bookid=""+search+""")
                        
                        myrec=cursor.fetchall()
                        for x  in myrec:
                            print(x)
                        cnx.close()


    
                    
                    Search_rec()



        ##TO  ADD STUDENT INFO#####
        print("---------------------------------------------------------------------STUDENT INFORMATION-----------------------------------------------------------")

        if(a==2):
            print("MAIN MENU")
            print("1.INSERT \t 2.DELETE  \t 3.Search")
            ch="i"
            while ch=="i":
                f=int(input("Enter ur choice:"))
                if (f==1):
                     n=int(input("Enter total no of student u want to insert...."))
                     for i in range(n):
                         def insert_data():
                             import mysql.connector
                             con=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                             cursor=con.cursor()
                             studentid=int(input("Enter student id"))
                             stud_name=input("Enter Student_name:")
                             f_name=input("Enter Father name")
                             age=int(input("Enter age:"))
                             qry=("insert into student values(%s,%s,%s,%s)")
                             data=(studentid,stud_name,f_name,age)
                             cursor.execute(qry,data)
                             con.commit()
                             cursor.close()
                             con.close()                
                             print("Record inserted")



                         def Display_rec():
                              import mysql.connector
                              cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                              print("Connection successfully")
                              cursor=cnx.cursor()
                              cursor.execute("select * from student")
                              myrec=100
                              myrec=cursor.fetchall()
                              for x  in myrec:
                                  print(x)
                              cnx.close()


    
                         insert_data()
                         Display_rec()


                if(f==2):
                    n=int(input("Enter total no of student u want to delete...."))
                    for i in range(n):
                        def delete_rec():
                            import mysql.connector
                            con=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                            cursor=con.cursor()
                            student_id=int(input("Enter student id"))
                            qry=("delete from student where studentid=student_id")
                            data=(student_id)
                            cursor.execute(qry,data)
                            con.commit()
                            cursor.close()
                            con.close()                
                            print("Record deleted ")





                
                        def Display_rec():
                            import mysql.connector
                            cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                            print("Connection successfully")
                            cursor=cnx.cursor()
                            cursor.execute("select * from student")
                            myrec=cursor.fetchall()
                            for x  in myrec:
                                print(x)
                            cnx.close()

                        delete_rec()
                        Display_rec()    



                if (f==3):
                    def Search_rec():
                          import mysql.connector
                          cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                          print("Connection successfully")
                          cursor=cnx.cursor()
                          search=input("Enter the id.......")
                          cursor.execute("select * from student where studentid=+search+")
                          for x  in cursor:
                             print(x)
                          cnx.close()
                        

                    
                    Search_rec()
                    

           
        

    
    ##TO  ADD RECORD IN ISSUE TABLE#######
        print("---------------------------------------------------------------ISSUE INFORMATION------------------------------------------------------------------------------")
        if (a==3):
              print("MAIN MENU")
              print("1.INSERT \t 2.DELETE \t 3.SEARCH")
              ch="i"
              while ch=="i":
                f=int(input("Enter ur choice:"))
                if (f==1):
                     n=int(input("Enter total no of book u want to issue today...."))
                     for i in range(n):
                           def insert_data():
                      
                                  import mysql.connector
                                  con=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                                  cursor=con.cursor()
                                  studentid=int(input("Enter student id"))
                                  bookid=int(input("Enter book id:"))
                                  book_name=input("Enter Book name")
                                  dd=int(input("Enter date"))
                                  mm=int(input("Enter month"))
                                  yy=int(input("Enter year"))
                                  qry=("insert into issue(studentid,bookid,book_name,dateofissue) values(%s,%s,%s,%s)")
                                  data=(studentid,bookid,book_name,date(yy,mm,dd))
                                  cursor.execute(qry,data)
                                  con.commit()
                                  cursor.close()
                                  con.close()                
                                  print("Record inserted")



                           def Display_rec():
                               import mysql.connector
                               cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                               print("Connection successfully")
                               cursor=cnx.cursor()
                               cursor.execute("select * from issue")
                               myrec=cursor.fetchall()
                               for x  in myrec:
                                   print(x)
                               cnx.close()


    
                           insert_data()
                           Display_rec()
         

                if(f==2):
                    def delete_rec():
                        import mysql.connector
                        con=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                        cursor=con.cursor()
                        book_id=int(input("Enter book id......"))
                        qry=("delete from issue where bookid=book_id")
                        data=(book_id,)
                        cursor.execute(qry,data)
                        con.commit()
                        cursor.close()
                        con.close()                
                        print("Record deleted ")

                    def Display_rec():
                
                        import mysql.connector
                        cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                        print("Connection successfully")
                        cursor=cnx.cursor()
                        cursor.execute("select * from issue")
                        myrec=cursor.fetchall()
                        for x  in myrec:
                            print(x)
                        cnx.close()



                    delete_rec()
                    Display_rec()      
                        

                    


              if (f==3):
               def Search_rec():
                   import mysql.connector
                   cnx=mysql.connector.connect(user="root",password="!@#$%^&",host="127.0.0.1",database="library")
                   print("Connection successfully")
                   cursor=cnx.cursor()
                   search=input("Enter the id.......")
                   cursor.execute("select * from student where studentid=+search+")
                   myrec=cursor.fetchall()
                   for x  in myrec:
                         print(x)
                   cnx.close()






         
               Search_rec()


               


else:
    print("Check your login id or password")    
