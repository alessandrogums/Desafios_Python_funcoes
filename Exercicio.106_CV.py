def ajuda():
    while True:
        print("~" * 30)
        print(" Sistema de ajuda para Python")
        print("~" * 30
      
        comando = str(input("Comando ou biblioteca ('fim' para): ")
       
        if comando.lower() == "fim":
            print("~" * 16)
            print(" Bye-Bye!")
            print("~" * 16)
            break
            
        print(help(comando))
        


ajuda()
