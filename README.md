# Keylogger con Webhook de Discord

Este es un keylogger simple que registra las pulsaciones de teclas y las envía periódicamente a un webhook de Discord.

## ⚠️ ADVERTENCIA
Este software es solo para fines educativos y debe usarse ÚNICAMENTE con consentimiento explícito. El uso no autorizado puede ser ilegal.

## Requisitos
- Python 3.6+
- Librerías especificadas en requirements.txt

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/keylogger-discord-webhook.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Edita el archivo `keylogger.py` y reemplaza `"TU_WEBHOOK_AQUI"` con tu webhook de Discord.

## Uso
Ejecuta el script:
```bash
python keylogger.py
```

## Características
- Registra teclas presionadas
- Maneja espacios, enters y backspaces correctamente
- Envía los logs a Discord mediante webhook
- Elimina los logs locales después de enviarlos

## Notas legales
El desarrollador no se hace responsable del mal uso de este software. Usa bajo tu propio riesgo y siempre con consentimiento.
```
