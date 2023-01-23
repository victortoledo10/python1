
import os
import validator


f_xml = input("Introduce el nombre del archivo XML: ")
f_xsd = input("Introduce el nombre del archivo XSD: ")


if validator.validate(f_xml, f_xsd):
    print('Valid! :)')
else:
    print('Not valid! :(')


# C:\Users\67740514\Downloads\Presupuestos_2023_SEDA_01.xml
#C:\Users\67740514\Downloads\presupuestos_entrada_PrincipalNoCesion_2023_2023-01-01.xsd



#import xml.etree.ElementTree as ET
#from xmlschema import XMLSchema
#from lxml import etree


# Cargar el archivo XML
#xml_tree = ET.parse("archivo.xml")

# Crear un objeto XMLSchema con el esquema XSD
#xsd_schema = XMLSchema("archivo.xsd")

# Validar el archivo XML contra el esquema XSD
#if xsd_schema.is_valid(xml_tree):
#    print("El archivo XML es válido según el esquema XSD")
#else:
#    print("El archivo XML no es válido según el esquema XSD")
