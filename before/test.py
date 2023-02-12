def run():
    totalFiles = 43
    numeros_lista = list(range(totalFiles+1))
    for i, numero in enumerate(numeros_lista):
        progress = i / totalFiles
        print(progress)


if __name__ == "__main__":
    run()
