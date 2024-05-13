```markdown
```markdown
# Diagrama de Clases
## Clases Principales
### Evento

+---------+
| Evento  |
+---------+
| - nombre: str
| - fecha: date
| - hora_apertura: time
| - hora_show: time
| - lugar: str
| - direccion: str
| - ciudad: str
| - estado: str
| - aforo_total: int
| - artistas: list[str]
| - tipo_evento: str
+---------+

### Boleta

+---------+
| Boleta  |
+---------+
| - comprador: Comprador
| - precio: float
| - tipo: str
| - fase_venta: str
| - estado: str
+---------+

### Boleteria

+----------+
| Boleteria |
+----------+
| - vender_boleta()
| - verificar_disponibilidad_aforo()
| - aplicar_descuentos()
| - emitir_boleta_cortesia()
| - generar_PDF_boleta()
+----------+

### Patrocinador

+--------------+
| Patrocinador |
+--------------+
| - nombre: str
| - valor_aportado: float
+--------------+

### Comprador

+------------+
| Comprador  |
+------------+
| - nombre: str
| - apellido: str
| - direccion: str
| - email: str
| - metodo_pago: str
+------------+

### Reporte

+--------+
| Reporte|
+--------+
| - generar_reporte_ventas_boletas()
| - generar_reporte_financiero()
| - generar_reporte_datos_compradores()
| - generar_reporte_datos_artista()
+--------+

### Dashboard

+---------+
| Dashboard|
+---------+
| - generar_dashboard()
+---------+

## Relaciones entre Clases

### Relación entre Evento y Boleta:
- Un Evento puede tener múltiples Boletas, pero una Boleta pertenece a un solo Evento. Por lo tanto, hay una relación de "1 a muchos" entre Evento y Boleta.

### Relación entre Boleta y Comprador:
- Una Boleta pertenece a un solo Comprador, pero un Comprador puede tener múltiples Boletas. Por lo tanto, hay una relación de "muchos a 1" entre Boleta y Comprador.

### Relación entre Boleteria y Boleta:
- La Tiquetera vende y gestiona las Boletas. Por lo tanto, hay una relación de "1 a muchos" entre Tiquetera y Boleta.

### Relación entre Evento y Patrocinador:
- Un Evento puede tener múltiples Patrocinadores y un Patrocinador puede patrocinar múltiples Eventos. Por lo tanto, hay una relación de "muchos a muchos" entre Evento y Patrocinador.

## Diagrama de Clases con Relaciones

```
```markdown
+---------+                +---------+
| Evento  |<>----------<>| Boleta  |
+---------+                +---------+
    ^                            |
    |                            |
    |                            v
    |                      +---------+
    |                      |Comprador|
    |                      +---------+
    |                            |
    |                            |
    +<------------<------------+

```
```markdown
+---------+                +--------------+
| Boleteria|<>---------<| Boleta       |
+---------+                +--------------+

```
```markdown
+---------+                +--------------+
| Evento  |<>--------<| Patrocinador|
+---------+                +--------------+

```
