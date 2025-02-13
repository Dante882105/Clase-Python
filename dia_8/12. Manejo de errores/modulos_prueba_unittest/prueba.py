# se importa la librería unittest desde python  
import unittest
# se importa el módulo a testear
import cambia_texto

#Se crea una clase para realizar la prueba con em método a utilizar de unittest como parámetro de la función
class Probar_cambia_texto(unittest.TestCase):
    #se crea una función para la prueba, la cual simepre deberá iniciar con la palabra "test"
    def test_mayusculas(self):
        #se crea la variable a usar para probar este test
        palabra = "buen día"
        #se trae el método del módulo y la función importado que será evaluado, en este caso "todo_mayusculas"
        resultado = cambia_texto.todo_mayusculas(palabra)
        #Se le inidca que se desea evaluar, para el caso será si el resultado es igual entre una y otra

        #ejecución ok
        self.assertEqual(resultado, 'BUEN DÍA')
        
        '''#Ejecución con error
        self.assertEqual(resultado, 'Buen Día')'''

#Utilizado para identificar la existencia del archivo main y al no estar presente, ignorarlo o no testear desde allí
if __name__ == '__main__':
    unittest.main()