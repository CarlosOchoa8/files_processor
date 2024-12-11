import xml.etree.ElementTree as et

file = et.parse("data.xml")

xml_path = [
    (
        "cfdi", {
        "TiposFiguraDomicilio": ("cfdi:Comprobante", "cfdi:Complemento" "cartaporte31:Cartaporte", "cartaporte31:FiguraTransporte", "cartaporte31:TiposFigura", "cartaporte31:Domicilio", "@Calle"),
        "UbicacionDomicilio": ("cfdi:Comprobante", "cfdi:Complemento" "cartaporte31:Cartaporte", "cartaporte31:Ubicaciones", "cartaporte31:Ubicacion", "cartaporte31:Domicilio", "@Pais")
    },
    )
]
for a, b in xml_path:
    # print(a)
    print(b)

data_to_dict = {
    "TiposFiguraDomicilio": [],
    "UbicacionDomcilio": []
}
