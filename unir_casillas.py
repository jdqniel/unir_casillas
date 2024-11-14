import os

import pandas as pd


def tiene_mayusculas(row):
    # Verifica si alguna de las columnas de la fila tiene contenido en mayúsculas
    return any(isinstance(x, str) and x.isupper() for x in row)


for file in os.listdir("problema3/data/"):
    if file.endswith(".xlsx"):
        filepath = os.path.join("problema3/data/", file)
        df = pd.read_excel(filepath, header=1, index_col=0)

        # Filtrar filas que cumplen ambas condiciones:
        # - Tienen texto en mayúsculas
        # - Tienen menos de 2 valores no nulos
        df = df[
            ~df.apply(lambda row: tiene_mayusculas(row) and row.count() < 2, axis=1)
        ]

        # Función para mover y unir valores de filas sin índice a la fila superior hasta que se llegue a una fila con índice válido
        def mover_y_unir_hasta_indice(df):
            cambios = True  # Asumimos que hubo cambios para iniciar el ciclo
            while cambios:  # Repetir mientras haya cambios
                cambios = (
                    False  # Inicializamos el flag de cambios como False para cada ciclo
                )
                # Recorremos las filas de abajo hacia arriba (excepto la primera)
                for i in range(len(df) - 1, 0, -1):
                    # Verificar si la fila actual no tiene índice (NaN) y tiene algún valor
                    if (
                        pd.isna(df.index[i]) and pd.notna(df.iloc[i]).any()
                    ):  # Fila sin índice y con contenido
                        # Recorremos las columnas para mover y unir los valores de cada celda
                        for column in df.columns:
                            # Si la celda actual tiene un valor
                            if pd.notna(df.iloc[i, df.columns.get_loc(column)]):
                                # Si la celda correspondiente en la fila anterior tiene valor
                                if pd.notna(df.iloc[i - 1, df.columns.get_loc(column)]):
                                    # Unir los valores, separándolos por un espacio
                                    df.iloc[i - 1, df.columns.get_loc(column)] = (
                                        str(df.iloc[i - 1, df.columns.get_loc(column)])
                                        + " "
                                        + str(df.iloc[i, df.columns.get_loc(column)])
                                    )
                                else:
                                    # Si la celda anterior está vacía, simplemente mover el valor
                                    df.iloc[i - 1, df.columns.get_loc(column)] = (
                                        df.iloc[i, df.columns.get_loc(column)]
                                    )
                                # Limpiar la celda actual
                                df.iloc[i, df.columns.get_loc(column)] = None
                                cambios = True  # Indicamos que hubo un cambio
                    # Si la fila superior tiene un índice válido, no movemos más valores hacia arriba
                    elif pd.notna(
                        df.index[i - 1]
                    ):  # Si la fila anterior tiene un índice válido
                        # En este caso, no se realizan más movimientos para esta fila
                        continue

            return df  # Devolvemos el DataFrame procesado

        # Llamar a la función para mover y unir los valores
        df_combinado = mover_y_unir_hasta_indice(df)

        # Eliminar filas que ya no tienen contenido en todas las columnas
        df_combinado.dropna(how="all", inplace=True)

        # Aplicar .strip() para eliminar espacios al principio y al final, y reemplazar múltiples espacios internos por uno solo
        df_combinado = df_combinado.applymap(
            lambda x: " ".join(str(x).split()) if isinstance(x, str) else x
        )

        # Guardar el resultado en un nuevo archivo de Excel
        df_combinado.to_excel(f"problema3/output/{file.split('.')[0]}.xlsx", index=True)

        # Verificar el resultado (opcional)
        print(df_combinado)
