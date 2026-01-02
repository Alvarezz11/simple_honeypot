# Simple Web Honeypot (Python)

Un Honeypot Web educativo desarrollado en Python. Simula un panel de administración falso para capturar intentos de login.

## Funcionalidad
El proyecto levanta un servidor web en el puerto `5000`.
- Muestra un panel de Login ("Administration Panel").
- **Captura cualquier credencial** (Usuario y Contraseña) que se intente usar.
- Muestra las credenciales robadas en la consola y las guarda en `honeypot.log`.

## Mapa del Proyecto
```bash
simple_honeypot/
├── templates/
│   └── login.html      # Plantilla HTML del panel de login
├── honeypot.log        # Logs de intentos de hackeo
├── main.py             # Aplicación principal (Flask)
├── requirements.txt    # Dependencias del proyecto
```

## Instalación y Uso

1. **Abrir en VSCode**.
2. **Instalar Dependencias**: Ejecuta `pip install -r requirements.txt` en la terminal.
3. **Ejecutar**: Presiona `F5` o corre `python main.py`.
4. **Probar**: Ve a tu navegador `http://localhost:5000`, escribe usuario/contraseña y mira la terminal.

## Nota Legal
Solo para fines educativos.
