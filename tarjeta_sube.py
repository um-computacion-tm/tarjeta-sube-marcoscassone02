class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = "primario"
PRECIO_TICKET = 70
DESACTIVADO = "desactivado"
ACTIVADO = "activado"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"

DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}

class Sube():
    def __init__(self):
        self.estado = ACTIVADO
        self.saldo = 0
        self.grupo_beneficiario = None
        
    
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == None:
            return PRECIO_TICKET
        else:
            for elemento in DESCUENTOS:
                if self.grupo_beneficiario == elemento:
                    ticket = PRECIO_TICKET - PRECIO_TICKET * (DESCUENTOS.get(elemento) / 100)
                    return ticket
                    
    def pagar_pasaje(self):
        self.obtener_precio_ticket()
        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException
        elif self.estado == "desactivado":
            raise UsuarioDesactivadoException
        else:
            self.saldo -= self.obtener_precio_ticket()
    
    def cambiar_estado(self,estado):
        if estado != ACTIVADO and estado != DESACTIVADO:
            raise EstadoNoExistenteException    
        self.estado = estado
    