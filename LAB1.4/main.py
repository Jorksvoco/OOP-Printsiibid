from devices import MyPrinter, Photocopier, MultiFunctionMachine

if __name__ == "__main__":
    printer = MyPrinter()
    photocopier = Photocopier()

    printer.print("Aastaaruanne.pdf")

    photocopier.print("Leping_v2.docx")
    photocopier.scan("Allkirjastatud_leping.pdf")

    mfm = MultiFunctionMachine(printer, photocopier)
    mfm.print("Delegated print task")
    mfm.scan("Delegated scan task")