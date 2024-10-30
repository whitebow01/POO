

## SQL con python

### fetchone y fetchall

´´´python
print(f"{rep['codrep']:10}{rep['nombre_repuesto']:20}{rep['fecha_fabricacion'].strftime('%d/%m/%Y') if isinstance(rep['fecha_fabricacion'], (datetime.date, datetime.datetime)) else rep['fecha_fabricacion']:18}{rep['precio_proveedor']:<18}{rep['precio_venta']:<15}{rep['peso']:<10}")
´´´

En este caso el código está accediendo a los datos usando índices, ya que `rep` es una **tupla** devuelta por `fetchone()`. Cuando realizas una consulta en MySQL y obtienes resultados con `fetchone()` o `fetchall()`, cada registro se devuelve como una tupla, donde cada elemento corresponde a una columna en el orden de la consulta SQL.

Por ejemplo, si tienes una consulta como esta:

```sql
SELECT codrep, nombre_repuesto, fecha_fabricacion, precio_proveedor, precio_venta, peso FROM repuestos;
```

Entonces, cada registro devuelto será una tupla como esta:

```python
rep = (codigo, nombre_repuesto, fecha_fabricacion, precio_proveedor, precio_venta, peso)
```

Accedes a cada elemento usando índices numéricos:

- `rep[0]` sería `codrep`.
- `rep[1]` sería `nombre_repuesto`.
- `rep[2]` sería `fecha_fabricacion`, y así sucesivamente.

