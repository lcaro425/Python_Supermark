from Databases import sqlite3

class Product:
    def __init__(self, productName="",unitCost="",productStock="",productDescription="",productId="",categoryId=0):
        self.__productId=productId
        self.__productName=productName
        self.__unitCost=unitCost
        self.__productStock=productStock
        self.__productDescription=productDescription
        self.__categoryId=categoryId
    
    @property
    def productId(self):
        return self.__productId
    
    @productId.setter
    def productId(self,productId):
        self.productId=productId

    @property
    def productName(self):
        return self.__productName
    
    @productName.setter
    def productName(self,productName):
        self.productName=productName

    @property
    def unitCost(self):
        return self.__unitCost
    
    @unitCost.setter
    def unitCost(self,unitCost):
        self.unitCost=unitCost

    @property
    def productStock(self):
        return self.__productStock
    
    @productStock.setter
    def productStock(self,productStock):
        self.productStock=productStock

    @property
    def productDescription(self):
        return self.__productDescription
    
    @productDescription.setter
    def productDescription(self,productDescription):
        self.productDesription=productDescription

    @property
    def categoryId(self):
        return self.__categoryId
    
    @categoryId.setter
    def categoryId(self,categoryId):
        self.categoryId=categoryId

    def __str__(self):
        return self.productName + "-" + str(self.__unitCost) + "-" + str(self.__productStock) + "-" + str(self.__productDescription) + "-" + str(self.__categoryId)

    def createProduct(self):
        db=sqlite3.Databases("supermark.db")
        self.__productName= input("Ingrese nombre del producto: ")
        self.__unitCost= input("Ingrese precio unitario del producto: ")
        self.__productStock= input("Ingrese stock del producto: ")
        self.__productDescription= input("Ingrese descripción del producto: ")
        category_table=db.select("category_table","categoryId,categoryName")
        print("Nro\tcategoryName")
        for category in category_table:
            print(f"{category_table[0]}\t{category_table[1]}")
        self.__categoryId=input("Ingrese la categoría del producto: ")
        db.insert("market_product_table","categoryId,productName,unitCost,productStock,productDescription",
                 f"{self.__categoryId},'{self.productName}','{self.unitCost}','{self.productStock}','{self.productDescription}'")
        db.close()

    def updateProduct(self,productId):
        db=sqlite3.Databases("supermark.db")
        print("Si no deea modificar este dato, presione Enter")
        print("hasta llegar al Dato que SI quiera modificar")
        market_product_table=db.select("market_product_table","cateogoryId","productName,unitCost,productStock,productDescription",f"productId={productId}")
        self.__productName= input(f"Modifique el nombre del producto: {market_product_table[0][1]} ") or market_product_table[0][1]
        self.__unitCost= input(f"Modifique el costo unitario del producto: {market_product_table[0][2]} ") or market_product_table[0][2]
        self.__productStock= input(f"Modifique el stock del producto: {market_product_table[0][3]} ") or market_product_table[0][3]
        self.__productDescription= input(f"Modifique la descripción del producto: {market_product_table[0][4]} ") or market_product_table[4][1]
        category_table=db.select("category_table","categoryId,categoryName")
        print("Nro\tcategory_table")
        for categoria in category_table:
            if market_product_table[0][0]==category_table[0][0]:
                productName=category_table[1]
        self.__categoryId=input(f"Modifique la categoría {productName}. Ingrese un número: ") or market_product_table[0][0]
        db.update("market_product_table","productName",f"'{self.__productName}'",f"productId={productId}")
        db.update("market_product_table","unitCost",f"'{self.__unitCost}'",f"productId={productId}")
        db.update("market_product_table","productStock",f"'{self.__productStock}'",f"productId={productId}")
        db.update("market_product_table","productDescription",f"'{self.__productDescription}'",f"productId={productId}")
        db.close()

    def deleteProduct(self,productId):
        db=sqlite3.Databases("supermark.db")
        db.update("market_product_table","0",f"productId={productId}")
        db.close()

    def listProduct(self,productId):
        db=sqlite3.Databases("supermark.db")
        db.cursor.execute("""SELECT P.productId,c.name AS category, p.productName,p.unitCost,p.productStock,p.productDescription
                            FROM market_product_table
                            INNER JOIN category_table
                            ON p.categoryId = c.categoryId""")
        db.close()

    def selectProduct(self,productId):
        db=sqlite3.Databases("supermark.db")
        market_products_table=db.select("market_product_table","productId,productName,unitCost,productStock,productDescription",f"categoryId={categoryId}")
        db.close()
        return market_products_table