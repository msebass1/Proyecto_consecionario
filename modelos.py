class Principal(object):

  def __init__(self, principal):
    self.Principal = principal

  def info(self,x, s):
    X = ''
    for dato in x:
      if dato == x[len(x)-1] and dato != 'Precio por hora' and dato != 'horas realizadas':
        T = input(f'Ingrese {dato} - {s}: ').center(25)
      elif (dato == 'Precio por hora' and s == 'servicio') or (dato == 'horas realizadas' and s == 'factura'):
        T = input(f'Ingrese {dato} - {s}: ')
        if self.__verificacion(T) == 'entero':
          T = T.center(25)
        else:
          print(f'\nValor no valido en {dato}, intentelo de nuevo')
          main()
          break
      else:
        T = input(f'Ingrese {dato} - {s}: ').center(25)
        T = T+'|'
      X += T
    return(X+'\n')

  def __verificacion(self, x):
    try:
      x = int(x)
      return 'entero'
    except ValueError:
      return 'No entero'

  def leerinfo(self,tipo):
    if tipo == 'cliente':
      datos = ['Id','Nombre','Apellido','Dirección','Teléfono','Ciudad']
    elif tipo == 'auto':
      datos = ['Placa','Marca','Modelo','Cilindrada','Color','Tipo','Combustibe','Número de Pasajeros','Capacidad de Carga','Número de Chasis','Número de Motor','Id_Dueño']
    elif tipo == 'servicio':
      datos = ['Codigo','Nombre','Precio por hora']
    elif tipo == 'factura':
      datos = ['Id_Cliente','Placa','CodigoServicio','horas realizadas']
    return self.info(datos, tipo)

  def ordenada(self, linea):
    X = linea.split("|")
    t = []
    for i in X:
      n = i.strip()
      t.append(n)
    return t

  def guardar(self, cad, nombre_archivo):
    baseDatos=open(nombre_archivo,"a") 
    baseDatos.write(cad)

  def leerBaseDatos(self,nombre_archivo):
    archivo = open(nombre_archivo,"r")
    resul = []
    contador=0
    for linea in archivo:
      palabras = self.ordenada(linea)
      if contador == 0:
        lin = palabras
        contador += 1
      else:
        a={}
        for i in range(len(palabras)):
          p = palabras[i].replace('\n','')
          l = lin[i].replace('\n','') 
          a[l]=p
        resul.append(a)
    return resul  
  
  def busqueda_identificador(self,archivo,tipo):
    lista = self.leerBaseDatos(archivo)
    ans = []
    print()
    w = input('Ingrese '+tipo+' a buscar: ')
    for diccionario in lista:
      if diccionario[tipo] == w:
        ans.append(diccionario)
    return ans

  def busqueda_orden(self,archivo,tipo):
      lista = self.leerBaseDatos(archivo)
      a = []
      sol=[]
      for diccionario in lista:
        a.append(diccionario[(tipo)])
      a.sort()
      for i in a:
        for diccionario in lista:
          if diccionario[tipo] == i and diccionario not in sol:
            sol.append(diccionario)
      return sol

  def visualizarBusqueda(self,lista,tipo):
    count=1
    for diccionario in lista:
      print('\n',tipo.capitalize(),count,'\n')
      for k,v  in diccionario.items():
        print(k.ljust(20,' '),' ',v)
      count += 1

class Persona(Principal):

  def busqueda(self):
    dic = {'1':'Id','2':'Nombre','3':'Apellido','4':'Dirección','5':'Teléfono','6':'Ciudad'}
    print('Seleccione como desea buscar: \n')
    print(' 1) Busqueda por orden \n 2) Busqueda por identificador\n')
    estado = input('¿Comó desea buscar?: ')
    print()
    sol = []
    if estado == '1':
      print('Seleccione el tipo de atributo con el que realizar la busqueda:\n')
      print(' 1) Id \n 2) Nombre \n 3) Apellido \n 4) Dirección \n 5) Teléfono \n 6) Ciudad \n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_orden('BD_clientes.txt',s)
        self.visualizarBusqueda(sol, 'Cliente')
      else:
        print()
        print('Opción invalida, Intentelo otra vez \n')
        self.busqueda()
    elif estado == '2':
      print('Seleccione el tipo de atributo con el que realizar la busqueda:\n')
      print(' 1) ID \n 2) Nombre \n 3) Apellido \n 4) Dirección \n 5) Teléfono \n 6) Ciudad \n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_identificador('BD_clientes.txt',s)
        self.visualizarBusqueda(sol, 'Cliente')
      else:
        print()  
        print('Opción invalida, Intentelo otra vez \n')
        self.busqueda()
    else:
      print('Opción Invalida, intentelo otra vez \n')
      self.busqueda()

class Vehiculo(Principal):

  def busqueda(self):
    dic = {'1':'Placa','2':'Marca','3':'Modelo','4':'Cilindrada','5':'Color','6':'Tipo','7':'Combustible','8':'Pasajeros','9':'Carga','10':'Chasis','11':'Motor','12':'Id_Dueño'}
    print('Seleccione como desea buscar:\n')
    print(' 1) Busqueda por orden \n 2) Busqueda por identificador\n')
    estado = input('¿Comó desea buscar?: ')
    if estado == '1':
      print('\nSeleccione el tipo de atributo con el que realizar la busqueda:\n')
      print(' 1) Placa \n 2) Marca \n 3) Modelo \n 4) Cilindrada \n 5) Color \n 6) Tipo \n 8) Capacidad de Pasajeros\n 9) Capacidad de carga\n 10) Número de chasis\n 11) Número del Motor \n 12) Id_Dueño\n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_orden('BD_autos.txt',s)
        self.visualizarBusqueda(sol, 'Automovil')
      else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.BIV()
    elif estado == '2':
      print('\n Seleccione el tipo de atributo con el que realizar la busqueda:\n')
      print(' 1) Placa \n 2) Marca \n 3) Modelo \n 4) Cilindrada \n 5) Color \n 6) Tipo \n 8) Capacidad de Pasajeros\n 9) Capacidad de carga\n 10) Número de chasis\n 11) Número del Motor \n 12) Id_Dueño\n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_identificador('BD_autos.txt',s)
        self.visualizarBusqueda(sol, 'Automovil')
      else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.busqueda()
    else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.busqueda()

class Servicio(Principal):

  def busqueda(self):
    dic = {'1':'Codigo','2':'Nombre','3':'Precio'}
    print('Seleccione como desea buscar\n')
    print(' 1) Busqueda por orden \n 2) Busqueda por identificador \n')
    estado = (input('¿Qué desea hacer?: '))
    if estado == '1':
      print('\n 1) Codigo \n 2) Nombre \n 3) Precio \n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_orden('BD_servicios.txt',s)
        self.visualizarBusqueda(sol, 'Servicio')
      else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.busqueda()
    elif estado == '2' :
      print(' \n 1) Codigo \n 2) Nombre \n 3) Precio \n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_identificador('BD_servicios.txt',s)
        self.visualizarBusqueda(sol, 'Servicio')
      else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.busqueda()
    else:
      print('\nOpción invalida, intentelo otra vez\n')
      self.busqueda()

class Factura(Principal):

  def busqueda(self):
    dic = {'1':'Codigofactura','2':'Id', '3':'Placa', '4':'CodigoServicio', '5':'Horas', '6':'Total'}
    print('Seleccione como desea buscar\n')
    print(' 1) Busqueda por orden \n 2) Busqueda por identificador \n')
    estado = input('¿Qué desea hacer?: ')
    if estado == '1':
      print(' \n 1) Codigofactura \n 2) Id \n 3) Placa \n 4) CodigoServicio \n 5) Horas\n 6) Total \n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_orden('BD_facturas.txt',s)
        self.visualizarBusqueda(sol, 'Factura')
      else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.busqueda()
    elif estado == '2' :
      print(' \n 1) Codigofactura \n 2) Id \n 3) Placa \n 4) CodigoServicio \n 5) Horas\n 6) Total \n')
      S = input('¿Cuál atributo escoge?: ')
      if S in dic.keys():
        s = dic[S]
        sol = self.busqueda_identificador('BD_facturas.txt',s)
        self.visualizarBusqueda(sol, 'factura')
      else:
        print()
        print('Opción invalida, intentelo otra vez\n')
        self.busqueda()
    else:
      print('\nOpción invalida, intentelo otra vez\n')
      self.busqueda()

  def __busqueda_especifica(self,bd,buscar,tipo):
    e = {'1':'Id','2':'Placa','3':'Codigo'}
    lista = self.leerBaseDatos(bd)
    w = buscar
    q = e[tipo]
    for diccionario in lista:
      if diccionario[q] == w:
        return diccionario

  def __numerofactura(self,txt):
    x = open(txt, "r")
    n=0
    for linea in x:
        if linea == '\n':
          pass
        else:
          n+=1    
    x.close()
    return n
  
  def crear_factura(self):
    a = self.leerinfo('factura')
    factura = self.ordenada(a)
    x = ''
    cliente = self.__busqueda_especifica('BD_clientes.txt',factura[0],'1')
    auto = self.__busqueda_especifica('BD_autos.txt',factura[1],'2')
    servicio = self.__busqueda_especifica('BD_servicios.txt', factura[2],'3') 
    if cliente != None and auto != None and servicio != None:
      if cliente['Id']== auto['Id_Dueño']:
        Codigofactura = self.__numerofactura('BD_facturas.txt')
        y = str(Codigofactura).center(25)
        t = list(servicio.values())
        pag = int(t[2])*int(factura[3])
        pagi = str(pag).center(25)
        a = y+'|'+a.rstrip('\n')+'|'+pagi+'\n'
        self.guardar(a, 'BD_facturas.txt')
        Codigofactura = int(Codigofactura)
        q = f'Factura-{Codigofactura}'.center(40)
        print('\n'+q+'\n')
        print('Datos del Usuario\n')
        for k,v in cliente.items():
          x += k.ljust(25)+v+'\n'
          print(k.ljust(25)+v)
        print('\nDatos del vehiculo\n')
        for k,v in auto.items():
          x += k.ljust(25)+v+'\n'
          print(k.ljust(25)+v)
        print('\nDatos del servicio realizado\n')
        for k,v in servicio.items():
          x += k.ljust(25)+v+'\n'
          print(k.ljust(25)+v)
        print('Horas del servicio'.ljust(25)+str(factura[3])+'\n')
        print('Valor total a pagar'.ljust(25)+str(pag))
        x += 'Horas del servicio'.ljust(25)+(factura[3])+'\n'
        x += 'Valor Total a pagar'.ljust(25)+str(pag)
        self.guardar(x,('factura_'+str(Codigofactura)))
      else:
        print('\nLos datos del cliente no corresponden a los de auto. Vuelva a realizar el proceso\n')
        self.crear_factura()
    else :
      print('\nUno de los parametros no está guardado, realice el proceso de nuevo\n')
      self.crear_factura()
