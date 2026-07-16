# Restaurante App

## Nombre del estudiante

SHERLYN ANGELICA VARGAS TAPUY

---

## Descripción

Este proyecto corresponde a un sistema de gestión básica para un restaurante desarrollado en Python utilizando Programación Orientada a Objetos.

Permite:

- Registrar productos.
- Registrar bebidas.
- Registrar clientes.
- Listar productos.
- Listar clientes.

---

## Estructura

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

---

## Responsabilidad de cada clase

### Producto

Representa un producto general del restaurante.

### Bebida

Hereda de Producto y agrega información específica como tamaño y tipo de envase.

### Cliente

Representa la información de un cliente.

### Restaurante

Administra el registro y listado de productos y clientes.

### main.py

Coordina la interacción mediante consola y llama a los métodos del servicio.

---

## Relación entre Producto y Bebida

Bebida hereda de Producto porque una bebida es un tipo de producto. Esto permite almacenar ambos objetos dentro de la misma colección y utilizar polimorfismo mediante el método `mostrar_informacion()`.

---

## Principios SOLID aplicados

### SRP (Responsabilidad Única)

Cada clase tiene una única responsabilidad.

### OCP (Abierto/Cerrado)

La clase Bebida amplía la funcionalidad mediante herencia sin modificar Restaurante.

### LSP (Sustitución de Liskov)

Los objetos Bebida pueden utilizarse como Producto dentro de la colección de productos.

---

## Ejecución

Entrar a la carpeta del proyecto y ejecutar:

```bash
python main.py
```

---

## Reflexión

Aplicar Programación Orientada a Objetos y los principios SOLID permite desarrollar sistemas organizados, reutilizables y fáciles de mantener. La separación de responsabilidades facilita agregar nuevas funcionalidades sin modificar el funcionamiento existente.# SEMANA8
