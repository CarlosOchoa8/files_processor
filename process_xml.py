import re
import xml.etree.ElementTree as ET

xml_tree = ET.parse("data.xml")
root = xml_tree.getroot()  # Obtén el nodo raíz del XML (el nodo <people>)

namespaces = {
    "cfdi": "http://www.sat.gob.mx/cfd/4"
}

dic = {
    "concepto_impuesto": ".//cfdi:conceptos//cfdi:traslados//cfdi:traslado[@Impuesto]",
    "impuesto_impuesto": ".//cfdi:impuestos//cfdi:traslados//cfdi:traslado[@Impuesto]"
}

for a, b in dic.items():
    print("aasdasddas", a,  b)

# Recorrer los paths definidos en el diccionario
for key, value in dic.items():
    traslado = root.find(value, namespaces)
    print(traslado)

    attrib_pattern = r"\[@([^\]]+)\]"
    attrib_name = re.search(attrib_pattern, value).group(1)
    if traslado is not None:
        print("++++++++++++++++++++++++++=")
        print(traslado.attrib[attrib_name])
        traslado = 0
    print("attrib_name ", attrib_name)
    print(f"KEY => {key} VALUE => {value} RESULTADO => {traslado.attrib.get(attrib_name, 0)}")

    if traslado is not None:
        impuesto_value = traslado.attrib.get(attrib_name, "No encontrado")
        print(f"  Impuesto: {impuesto_value}")
