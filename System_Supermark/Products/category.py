from Databases import sqlite3

class category:
    def __init__(self,categoryName="",categoryDescription="",categoryId=0):
        self.__categoryId=categoryId
        self.__categoryName=categoryName
        self.__categoryDescription=categoryDescription

    @property
    def categoryId(self):
        return self.__categoryId

    @categoryId.setter
    def categoryId(self,categoryId):
        self.__categoryId=categoryId

    @property
    def categoryName(self):
        return self.__categoryName

    @categoryName.setter
    def categoryName(self,categoryName):
        self.__categoryName=categoryName   

    @property
    def categoryDescription(self):
        return self.__categoryDescription

    @categoryDescription.setter
    def categoryDescription(self,categoryDescription):
        self.__categoryDescription=categoryDescription

    def create_category(self):
        categoryName=input("Ingrese nombre de la categoría: ")
        categoryDescription=input("Ingrese la descriptión de la categoría: ")
        db=sqlite3.Databases("supermark.db")
        db.insert("category_table","categoryName,categoryDescription",f"'{categoryName}','{categoryDescription}'")
        db.close()

    def update_category(self,categoryId):
        db=sqlite3.Databases("spermark.db")
        print("Si desea modificar un Dato, solo presione Enter")
        print("hasta llegar al Dato que desea actualizar.")
        category_table=db.select("category_table","categoryId,categoryName,categoryDescription",f"categoryId={categoryId}")
        self.__categoryName=input(f"Modifique el nombre de la Categoría: {category_table[0][1]}") or category_table[0][1]
        self.__categoryDescription=input(f"Modifique la descripción de la Categoría: {category_table[0][2]}") or category_table[0][2]
        db.update("category_table","categoryName",f"'{self.__categoryName}'",f"categoryId={categoryId}")
        db.update("category_table","categoryDescription",f"'{self.__categoryDescription}'",f"categoryId={categoryId}")
        db.close()

    def delete_category(self,categoryId):
        db=sqlite3.Databases("supermark.db")
        db.update("category_table","0",f"cateogryId={categoryId}")
        db.close()

    def list_category(self):
        db=sqlite3.Databases("spermark.db")
        category_table=db.select_all("category_table","categoryId,categoryName,categoryDescription")
        """print("NRO     Nombre     Descripción")
        for category in category_table:
            print(f"{category[0]} - {category[1]} - {category[2]}) """
        db.close()
        return category_table