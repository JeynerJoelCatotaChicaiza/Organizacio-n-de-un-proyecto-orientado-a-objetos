def chat_uea():
    print("\n🤖 CHATUEA - Universidad Estatal Amazónica")
    print("Escribe 'salir' para terminar.\n")

    while True:
        mensaje = input("Tú: ")

        if mensaje.lower() == "salir":
            print("CHATUEA: ¡Hasta luego! 👋")
            break

        elif "hola" in mensaje.lower():
            print("CHATUEA: ¡Hola! ¿En qué puedo ayudarte hoy? 😊")

        elif "tarea" in mensaje.lower():
            print("CHATUEA: Puedo ayudarte con tus tareas de Programación Orientada a Objetos.")

        elif "python" in mensaje.lower():
            print("CHATUEA: Python es un lenguaje ideal para trabajar con POO. ¿Qué tema deseas repasar?")

        elif "clase" in mensaje.lower():
            print("CHATUEA: Estoy aquí para apoyarte en tus clases. ¿Sobre qué tema tienes dudas?")

        elif "gracias" in mensaje.lower():
            print("CHATUEA: ¡Con gusto! 😄")

        else:
            print("CHATUEA: Interesante. Cuéntame más o dime cómo puedo ayudarte.")

if __name__ == "__main__":
    chat_uea()
