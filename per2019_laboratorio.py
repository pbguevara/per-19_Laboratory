class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name
        
    def get_price(self):
        return self.price
        
        
class Medicine(Product):
    def __init__(self, name, price, compound, percentage):
        self.name = name
        self.price = price
        self.compound = compound
        self.percentage = percentage
    
    def get_compound(self):
        return self.compund
        
    def get_percentage(self):
        return self.percentage
        

class Laboratory():
    def __init__(self, name, products_list):
        self.name = name
        self.products_list = products_list
        
    def get_name(self):
            return self.name
            
    def get_list(self):
        products = []
        for i in range(len(self.products_list)):
            product = self.products_list[i].get_name()
            products.append(product)
        return products
                
            
lab1_productos = []
lab2_productos = []

jarabe = Medicine("Jarabe", 7.25, "Glucosa", 0.5)
lab1_productos.append(jarabe)
lab2_productos.append(jarabe)

paracetamol = Medicine("Paracetamol", 3.50, "Povidona", 0.9)
lab1_productos.append(paracetamol)

ibuprofeno = Medicine("Ibuprofeno", 2.75, "Ácido esteárico", 0.7)
lab2_productos.append(ibuprofeno)

jabon = Product("Jabon", 4.30)
lab1_productos.append(jabon)
lab2_productos.append(jabon)

crema = Product("Crema", 8.0)
lab1_productos.append(crema)

labA = Laboratory("Roche", lab1_productos)
labB = Laboratory("Johnson&Johnson", lab2_productos)
laboratorios = [labA, labB]

for laboratorio in laboratorios:
    print("El laboratorio", laboratorio.get_name(), "tiene", laboratorio.get_list())


