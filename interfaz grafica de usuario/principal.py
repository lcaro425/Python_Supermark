importar  tkinter  como  tk
de  tkinter  importar  ttk
desde el cuadro de  mensaje de importación de tkinter  

clase  Principal ( tk . Tk ):
    def  __init__ ( auto ):
        súper (). __inicio__ ()
        uno mismo título ( "Menú Principal" )
        uno mismo geometría ( "1080x900" )
        uno mismo iconbitmap ( 'GUI/imagen/iconos/tienda.ico' )
        uno mismo foto  =  Ninguno
        #self.redimensionable (Falso, Falso)
        uno mismo configuración de columna ( 0 , peso  =  3 )
        uno mismo configuración de columna ( 1 , peso  =  3 )
        uno mismo configuración de columna ( 2 , peso  =  3 )
        uno mismo configuración de columna ( 3 , peso  =  3 )
        uno mismo configuración de columna ( 4 , peso  =  3 )
        uno mismo _crear_menú ()
        uno mismo _create_boton_action ()

    # Crear el menú   
    def  _create_menu ( auto ):
        uno mismo menú  =  tk . Menú ( auto )
        uno mismo config ( menú = self . menú )
        # Crear el menú de opciones
        opciones_menu  =  tk . Menú ( automenú ) _ _
        uno mismo menú _ add_cascade ( label = 'Opciones' , menu = opciones_menu )
        #opciones_menu.add_command(label='Login', command=self._login)
        #opciones_menu.add_command(label='Salir', command=self.destroy)
        #opciones_menu.add_command(label='Iniciar sesión')
        menú_opciones . add_command ( etiqueta = 'Salir' )
        # Crear el menú de ayuda
        ayuda_menu  =  tk . Menú ( menú propio , corte = 0 ) _
        uno mismo menú _ add_cascade ( etiqueta = 'Ayuda' , menu = ayuda_menu )
        #ayuda_menu.add_command(label='Acerca de', command=self._acerca_de)
        ayuda_menú . add_command ( label = 'Acerca de' )

    
    def  _create_boton_action ( auto ):
        uno mismo foto  =  tk . FotoImagen ( archivo  =  r"GUI/image/img/cliente.png" )
        uno mismo foto1  = conocimientos  tradicionales . FotoImagen ( archivo  =  r"GUI/image/img/producto.png" )
        uno mismo foto2  = conocimientos  tradicionales . FotoImagen ( archivo  =  r"GUI/image/img/venta.png" )
        uno mismo foto4  = conocimientos  tradicionales . FotoImagen ( archivo  =  r"GUI/image/img/pdf.png" )
        uno mismo foto5  = conocimientos  tradicionales . PhotoImage ( archivo  =  r"GUI/image/img/info.png" )

        btnInfo  =  tk . Botón ( auto , imagen  =  auto . foto , ancho  =  50 , altura  =  50 , comando  =  auto . _list_client )
        btnInfo1  =  tk . Botón ( self ,   imagen  =  self . foto1 , ancho = 50 , alto = 50 ,   comando  =  self . _list_producto )
        btnInfo2  =  tk . Botón ( self , image  =   self . photo2 , width = 50 , height = 50 ,   command  =  self . _list_sale )
        btnInfo3  =  tk . Botón ( auto , imagen  =  auto . foto4 , ancho  =  50 , altura  =  50 )
        btnInfo4  =  tk . Botón ( auto , imagen  =  auto . foto5 , ancho  =  50 , altura  =  50 )

        btnInfo . cuadrícula ( fila  =  1 , columna  =  0 , adhesivo = "NWE" )
        btnInfo1 . cuadrícula ( fila  =  1 , columna  =  1 , adhesivo = "NWE" )
        btnInfo2 . cuadrícula ( fila  =  1 , columna  =  2 , adhesivo = "NWE" )
        btnInfo3 . cuadrícula ( fila  =  1 , columna  =  3 , adhesivo = "NWE" )
        btnInfo4 . cuadrícula ( fila  =  1 , columna  =  4 , adhesivo = "NWE" )


    def  _list_client ( auto ):
        árbol  =  ttk . Treeview ( auto , columna = ( "c1" , "c2" , "c3" , "c4" ), show = 'encabezados' )
        árbol _ columna ( "#1" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#1" , texto = "Nro" )
        árbol _ columna ( "#2" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#2" , texto = "Apellido" )
        árbol _ columna ( "#3" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#3" , texto = "Nombre" )
        árbol _ columna ( "#4" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#4" , texto = "Documento" )
        árbol _ columna ( "#4" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#4" , texto = "Domicilio" )
        árbol _ cuadrícula ( fila  =  2 , columna  =  0 , sticky = "SWE" , columnpan = 5 , padx  =  10 , pady  =  10 )
        uno mismo img_create_person  =  tk . PhotoImage ( archivo  =  r"GUI/image/img/add_persona.png" )
        uno mismo img_edit_person  =  tk . PhotoImage ( archivo  =  r"GUI/image/img/editar_persona.png" )
        uno mismo img_delete_person  =  tk . FotoImagen ( archivo  =  r"GUI/image/img/delete_persona.png" )
        btn_create  = conocimientos  tradicionales . Botón ( auto , imagen  =  auto . img_create_person , ancho  =  50 , alto  =  50 )
        btn_create . cuadrícula ( fila  =  3 , columna  =  0 , adhesivo = "SWE" , padx  =  10 )
        btn_create  = conocimientos  tradicionales . Botón ( self , image  =  self . img_edit_person , ancho  =  50 , altura  =  50 )
        btn_create . cuadrícula ( fila  =  3 , columna  =  1 , adhesivo = "SWE" , padx  =  10 )
        btn_create  = conocimientos  tradicionales . Botón ( self , image  =  self . img_delete_person , ancho  =  50 , alto  =  50 )
        btn_create . cuadrícula ( fila  =  3 , columna  =  2 , adhesivo = "SWE" , padx  =  10 )

    """ def _list_client(self):
        filas = []
        para i en el rango (2,5):
            columnas = []
            para j en el rango (0,5):
                e = tk.Entrada(relieve = tk.SURCO)
                e.grid(fila=i, columna=j, fijo = tk.NSEW)
                e.insert(tk.END, '%d.%d' % (i, j))
                cols.append(e)
            filas.append(columnas) """
    
    def  _list_sale ( auto ):
        árbol  =  ttk . Treeview ( auto , columna = ( "c1" , "c2" , "c3" , "c4" ), show = 'encabezados' )
        árbol _ columna ( "#1" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#1" , texto = "Nro" )
        árbol _ columna ( "#2" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#2" , texto = "Cliente" )
        árbol _ columna ( "#3" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#3" , texto = "Fecha" )
        árbol _ columna ( "#4" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#4" , texto = "Total" )
        árbol _ cuadrícula ( fila  =  2 , columna  =  0 , sticky = "SWE" , columnpan = 5 , padx  =  10 , pady  =  10 )
        

    def  _list_producto ( auto ):
        árbol  =  ttk . Treeview ( auto , columna = ( "c1" , "c2" , "c3" , "c4" ), show = 'encabezados' )
        árbol _ columna ( "#1" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#1" , texto = "Nro" )
        árbol _ columna ( "#2" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#2" , texto = "Nombre" )
        árbol _ columna ( "#3" , ancla = tk . CENTRO )
        árbol _ encabezado ( "# 3" , texto = "Stock" )
        árbol _ columna ( "#4" , ancla = tk . CENTRO )
        árbol _ encabezado ( "#4" , texto = "Precio" )
        árbol _ cuadrícula ( fila  =  2 , columna  =  0 , sticky = "SWE" , columnpan = 5 , padx  =  10 , pady  =  10 )
        
si  __nombre__  ==  '__principal__' :
    aplicación  =  principal ()
    aplicación _ bucle principal () 
