import numpy as np

class Graphs:

    def __init__(self, ord : int , direction : bool , pondered : bool):

        self.matriz = np.zeros((ord,ord))
        self.ispondered = pondered #true if the grapf is pondered

        def __InitMatriz():
            for item in matriz:
                item = None

        def Exist(v1 , v2) :
            if matriz[v1-1][v2-1] != None : return True
            else : return False


        def Insert(v1, v2, ponder = 1):
            if( ispondered ):
                InsertRelation(v1 , v2, pondered)
            else:
                InsertRelation(v1 , v2 , 1)     
                return True
        
        def InsertRelation(v1 , v2, ponder):
            if matriz[v1-1][v2-1] is not None :
                return False
            else :
                if ispondered:
                    matriz[v1-1][v2-1] = ponder
                else : 
                    matriz[v1-1][v2-1] = 1

                return True

        def Remove(v1 , v2):
            if Exist( v1 , v2) :
                matriz[v1-1][v2-1] = None
            
            return True

        def NeighborVertives(v):
            if v-1 > ord or v-1 < 0: return

            list_of_entry = []
            list_of_exit= []
            cont = 0
            for x in range(ord):
                if matriz[v-1][x] != 0 :
                    list_of_entry.append(x+1)
            
            for x in range(ord):
                if matriz[x][v-1] != 0 :
                    list_of_exit.append(x+1)

            return  list_of_entry , list_of_exit
                    
            


