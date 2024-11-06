

class Jugador:
    def __init__(self,id_jugador,nombre,apellido,nickname,contrasenia,salt) -> None:
        self.__id_jugador = id_jugador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nickname = nickname
        self.__contrasenia = contrasenia
        self.__salt = salt
        
    
    def get_id_jugador(self):
        return self.__id_jugador
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_nickname(self):
        return self.__nickname
    def get_contrasenia(self):
        return self.__contrasenia
    def get_salt(self):
        return self.__salt
    

    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_nickname(self,alias):
        self.__nickname = alias
    def set_contrasenia(self,clave_nueva):
        self.__contrasenia = clave_nueva
        
    

    def __str__(self):
        return f"jugador [id= {self.__id_jugador}, nombre= {self.__nombre}, apellido={self.__apellido},  nickname(alias)= {self.__nickname} ]"
    



    
    
    