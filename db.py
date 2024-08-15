# --host=Eska0328.mysql.pythonanywhere-services.com
# Database host address:Eska0328.mysql.pythonanywhere-services.com
# Username:Eska0328
# CREATE TABLE IF NOT EXISTS `Eska0328$Data`.`user` (
#   `ID` INT NOT NULL AUTO_INCREMENT,
#   `username` VARCHAR(16) NOT NULL,
#   `email` VARCHAR(255) NOT NULL,
#   `password` VARCHAR(32) NOT NULL,
#   `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
#   `data` FLOAT NOT NULL DEFAULT 0,
#   `usercol` VARCHAR(45) NULL,
#   UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
#   PRIMARY KEY (`ID`))
# ENGINE = InnoDB
# 
# 
# 
# 
#  lmCsGC0QmRv8mUk
import mysql.connector

def connecter():
    mydb = mysql.connector.connect(
        host="Eska0328.mysql.pythonanywhere-services.com",
        user="Eska0328",
        password="Suhee123455"
    )
    return mydb

# sql = "INSERT INTO user (username, email, password, data) VALUES (%s, %s, %s, %s)"
# val = ("John", "John@gmail.com", "password", "")
# mycursor.execute(sql, val)

# mydb.commit()



# mycursor.execute("SELECT * FROM user")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)