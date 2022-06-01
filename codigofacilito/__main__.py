from codigofacilito import unreleased

#Forma profecional de imprimir en pantalla
import logging

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""
#para q en consola se imprima desde el lvl DEBUG x default es desde WARNING

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug(">>> Estamos comenzando la ejecucion del paquete")
    workshops = unreleased()
    logging.debug(workshops)

    logging.debug(">>> Estamos finalizando la ejecucion del paquete")