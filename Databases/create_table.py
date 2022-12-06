import sqlite3

db=sqlite3.DataBase("supermark.db")
 
#NORMAL USER=1 / SUPERMARKET STOCK USER=0
db.create_table("rol","rolId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                        "username TEXT,"+
                        "userDescription TEXT,"+
                        "userStatus INTEGER DEFAULT 1"
                )

#ACTIVE USER=1 / INACTIVE USER=0
db.create_table("client",
                "userId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "username TEXT,"+
                "userPass TEXT,"+
                "userFirstName TEXT,"+
                "userLastName TEXT,"+
                "userDNI INTEGER,"+
                "userBirthdate TEXT(10),"+
                "userPhone TEXT(9)"
                "userEmail TEXT(50),"+
                "userRegisterDate TEXT(10),"+
                "userStatus INTEGER DEFAULT 1,"+
                "userAddress TEXT,"+
                "userPaymentCard INTEGER"
                "rolId INTEGER"
                )

db.create_table("category",
                "categoryId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "categoryName TEXT(100),"+
                "categoryDescription TEXT(200)"
                )

db.create_table("market_product",
                "productId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "categoryId INTEGER,"+
                "productName TEXT(200),"+
                "unitCost REAL,"+
                "productStock INTEGER,"+
                "productDescription TEXT(200)"
                )

db.create_taable("basket",
                "basketId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "poductId INTEGER,"+
                "productQuantity INTEGER,"+
                "productAddDate TEXT(10)"
                )

#STATUS =1 APPROVED / STATUS=0 NOT APPROVED
#APPROVAL=0 NOT PAYED / APPROVAL=1 PAYED
db.create_table("order",
                "orderId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "orderDate TEXT(10),"+
                "orderTotal REAL,"+
                "orderItemsNumber INTEGER,"+
                "clientId INTEGER,"+
                "orderStatus INTEGER DEFAULT 1,"+
                "paymentApproval INTEGER DEFAULT 0"
                )

#STATUS =1 SHIPPED / STATUS=0 NOT SHIPPED
db.create_table("shipping_details",
                "shippingId INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "orderId INTEGER,"+
                "shippingStatus INTEGER DEFAULT 0",+
                "shippingCost REAL"
                )

db.close()