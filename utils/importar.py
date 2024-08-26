import csv

def Importar():

    results = []
    with open('utils/plano.csv', encoding='UTF-8') as File:
        reader = csv.DictReader(File, delimiter=';')
        for row in reader:
            results.append({
                "cedula": str(row["cedula"]),
                "apellido1": str(row['apellido1']),
                "apellido2": str(row['apellido2']),
                "nombre1": str(row['nombre1']),
                "nombre2": str(row['nombre2']),
                "genero": str(row['genero']),
                "nacimiento": str(row['nacimiento']),
                "sanguineo": str(row['sanguineo']),
                "contacto": str(row['contacto']),
                "telefono_contacto": str(row['telefono_contacto']),
                "contacto1": str(row['contacto1']),
                "telefono_contacto1": str(row['telefono_contacto1']),
                "arl": str(row['arl']),
                "eps": str(row['eps']),
                "centro_id": int(row['centro_id']),
                "activo": bool(row['activo'])
            })
            print(row['cedula'], row['nombre1'])
    return results