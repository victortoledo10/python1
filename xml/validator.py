from lxml import etree

def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    if result:
        print("El archivo XML es válido según el esquema XSD.")
    else:
        print("El archivo XML NO es válido según el esquema XSD.")
        for error in xmlschema.error_log:
            print(error.message)


    return result


