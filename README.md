Aquí tienes el README actualizado para crear un entorno virtual con `venv` antes de instalar las dependencias:

---

# Procesamiento de Archivos Excel - Filtrado y Unificación de Datos

Este script procesa archivos de Excel en una carpeta específica, aplicando filtros y transformaciones para depurar y combinar información de filas sin índices, que están fuera de posición. Los archivos procesados se guardan en una nueva carpeta de salida.

## Requisitos

Para mantener el entorno de trabajo limpio y ordenado, primero crearemos un entorno virtual y luego instalaremos los paquetes necesarios.

### Paso 1: Crear un Entorno Virtual

En la terminal, navega hasta la carpeta del proyecto y ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

```bash
python3 -m venv venv
```

Esto generará una carpeta llamada `venv` dentro del proyecto, donde se instalarán las dependencias necesarias.

### Paso 2: Activar el Entorno Virtual

- **En Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **En macOS y Linux**:
  ```bash
  source venv/bin/activate
  ```

Verás que el entorno virtual está activado cuando el nombre `(venv)` aparezca al inicio de la línea en tu terminal.

### Paso 3: Instalar Dependencias

Una vez activado el entorno virtual, instala las dependencias desde el archivo `requirements.txt` con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

- `problema3/data/`: Carpeta de entrada donde deben colocarse los archivos `.xlsx` que serán procesados.
- `problema3/output/`: Carpeta de salida donde se guardarán los archivos procesados en formato `.xlsx`.
- `script.py`: Archivo que contiene el script Python con el procesamiento.
- `requirements.txt`: Archivo con la lista de dependencias necesarias.

## Funcionamiento del Script

1. **Carga de Archivos Excel**: El script carga cada archivo `.xlsx` ubicado en la carpeta `problema3/data/`, omitiendo la primera fila como encabezado y configurando la primera columna como índice.

2. **Filtrado de Filas**: Se eliminan las filas que cumplen ambas condiciones:
   - Contienen al menos un texto en mayúsculas.
   - Tienen menos de dos valores no nulos en todas las columnas.

3. **Unificación de Filas sin Índice**: Las filas sin índice (con `NaN` como índice) que contienen valores se combinan con la fila superior:
   - Si ambas celdas en una columna contienen valores, estos se unen.
   - Si la celda de la fila superior está vacía, el valor de la fila actual se mueve hacia arriba.
   - Este proceso continúa hasta alcanzar una fila con índice válido.

4. **Limpieza de Filas Vacías**: Después de mover y unir los valores, se eliminan las filas que ya no contienen datos en todas las columnas.

5. **Depuración de Espacios**: En los valores de texto, se eliminan los espacios en blanco iniciales y finales y se reemplazan múltiples espacios internos por uno solo.

6. **Guardar Resultado**: El DataFrame resultante se guarda en un nuevo archivo en la carpeta `problema3/output/`.

## Ejecución del Script

Para ejecutar el script, asegúrate de estar en la misma carpeta donde se encuentra el archivo `script.py` y con el entorno virtual activado. Luego, ejecuta:

```bash
python unir_casillas.py
```

Esto procesará todos los archivos `.xlsx` en la carpeta `problema3/data/` y guardará los archivos modificados en `problema3/output/`.

---

## Ejemplo de Uso

Si tienes un archivo `example.xlsx` en la carpeta `problema3/data/`, al ejecutar el script, se creará un archivo `example.xlsx` en la carpeta `problema3/output/` con los datos filtrados y unificados según las reglas mencionadas.

---

## Verificación

Al final del procesamiento, el script imprime el contenido de cada archivo procesado. Puedes desactivar esta funcionalidad opcional removiendo o comentando la línea `print(df_combinado)` si no deseas ver los resultados en la consola.

--- 

Recuerda desactivar el entorno virtual cuando hayas terminado de trabajar ejecutando el comando `deactivate`.
