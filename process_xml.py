import re
import xml.etree.ElementTree as ET
import pandas as pd

xml_tree = ET.parse("data.xml")
root = xml_tree.getroot()  # Obtén el nodo raíz del XML (el nodo <people>)

namespaces = {
    "cfdi": "http://www.sat.gob.mx/cfd/4",
    "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital",
    "cartaporte31": "http://www.sat.gob.mx/CartaPorte31"
}

mapping_attribs = {
    "concepto_impuesto": ".//cfdi:Conceptos//cfdi:Traslados//cfdi:Traslado[@Impuesto]",
    "concepto_impuesto": ".//cfdi:Conceptos//cfdi:Traslados//cfdi:Traslado[@Impuesto]",
    "impuesto_impuesto": ".//cfdi:Complemento//cartaporte31:CartaPorte[@Version]",
    "impuesto_retencion": ".//cfdi:Impuestos//cfdi:Retenciones//cfdi:Retencion[@TipoFactor]",
    "uuid": ".//cfdi:Complemento//tfd:TimbreFiscalDigital[@UUID]",
    "cliente": ".//cfdi:Receptor[@Rfc]",
    "conceptoTraslado": ".//cfdi:Complemento//tfd:TimbreFiscalDigital[@UUID]",
    "impuestoTraslado": ".//cfdi:Complemento//cartaporte31:CartaPorte//cartaporte31:Mercancias//cartaporte31:Mercancia[@BienesTransp]",
    "impuestoRetencion": ".//cfdi:Complemento//cartaporte31:CartePorte//cartaporte31:Mercancias//cartaporte31:Mercancia[@Cantidad]",
    # "clienteRfc": "CONSTANTE"
}

attribs_data = {
    "conceptoTraslado": [],
    "ImpuestoTraslado": [],
    "Impuest oRetencion": [],
    "clienteRfc": [],
    "cfdi": [],
    "claveSubProducto": [],
    "volumenIT": [],
    "volumenFT": [],
    "terminalAlmYDist": [],
    "permisoAlmYDist": [],
    "temperatura": [],
    "presionAbsoluta": [],
    "fechaYHIM": [],
    "fechaYHFM": [],
    "tipo": [],
    "movimiento": [],
    "rfcCliente": []
}


# Recorrer los paths definidos en el diccionario
attrib_pattern = r"\[@([^\]]+)\]"
for key, value in mapping_attribs.items():
    attrib_name = re.search(attrib_pattern, value).group(1)
    find_attrib = root.find(value, namespaces)

    if find_attrib is not None:
        attrib_value = find_attrib.get(attrib_name, "No existe el atributo.")
        print("Attrib =>", attrib_name, "|", key)
        print("Attrib Value =>",  attrib_value)
        # attribs_data.update()

    if find_attrib is None:
        find_attrib = 0
        continue
    # print(find_attrib.attrib[attrib_name])
    # print(find_attrib.attrib.get(attrib_name, "No"))
    # print(f"KEY => {key} VALUE => {value} RESULTADO => {find_attrib.attrib.get(attrib_name, 0)}")


# 'cfdi': ('cfdi:Comprobante', 'cfdi:Complemento', 'tfd:TimbreFiscalDigital','@UUID')
# "claveSubProducto": ("cfdi:Comprobante", "cfdi:Complemento", "cartaporteXX:CartaPorte", "cartaporteXX:Mercancias", "cartaporteXX:Mercancia", "@BienesTransp"),
# 'volumenIT': ('cfdi:Comprobante', "cfdi:Complemento", "cartaporteXX:CartaPorte", "cartaporteXX:Mercancias", "cartaporteXX:Mercancia", "@Cantidad"),
# 'volumenFT': ("cfdi", ),
# 'terminalAlmYDist': ("cfdi", ),
# 'permisoAlmYDist': ("cfdi", ),
# 'temperatura': ("cfdi", ),
# 'presionAbsoluta': ("cfdi", ),
# 'fechaYHIM': ("cfdi:Comprobante", "cfdi:Complemento", "cartaporteXX:CartaPorte", "cartaporteXX:Ubicaciones","cartaporteXX:Ubicacion", "@FechaHoraSalidaLlegada"),
# 'fechaYHFM': ("cfdi:Comprobante", "cfdi:Complemento", "cartaporteXX:CartaPorte", "cartaporteXX:Ubicaciones","cartaporteXX:Ubicacion", "@FechaHoraSalidaLlegada"),
# 'tipo': "Nacional",
# 'movimiento': "Entrega",
# 'rfcCliente': ('cfdi:Comprobante', 'cfdi:Emisor', '@Rfc'),