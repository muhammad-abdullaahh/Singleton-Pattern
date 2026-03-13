class Printer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating Printer instance...")
            cls._instance = super(Printer, cls).__new__(cls)
        return cls._instance

    def print_document(self, document):
        print(f"Printing document: {document}")

printer1 = Printer()
printer2 = Printer()

printer1.print_document("Report.pdf")

print(printer1 is printer2)  
