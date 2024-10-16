class Property:
    def __init__(self, property_id, address, price, type_, status, owner):
        self.property_id = property_id
        self.address = address
        self.price = price
        self.type_ = type_
        self.status = status  # 'Available' or 'Sold'
        self.owner = owner  # Owner of the property (Seller)

    def __str__(self):
        return f"ID: {self.property_id}, Address: {self.address}, Price: {self.price}, Type: {self.type_}, Status: {self.status}"

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role  # 'Buyer', 'Seller', or 'Agent'

    def __str__(self):
        return f"{self.name} ({self.role})"

class RealEstateSystem:
    def __init__(self):
        self.properties = []  # List to store all properties
        self.users = []  # List to store all users
        self.transactions = []  # List to store all transactions

    def add_property(self, address, price, type_, owner):
        property_id = len(self.properties) + 1  # Simple ID generator
        new_property = Property(property_id, address, price, type_, 'Available', owner)
        self.properties.append(new_property)
        print(f"Property '{address}' added successfully.")

    def list_properties(self):
        if not self.properties:
            print("No properties available.")
        else:
            for property in self.properties:
                print(property)

    def register_user(self, name, role):
        user_id = len(self.users) + 1
        new_user = User(user_id, name, role)
        self.users.append(new_user)
        print(f"User '{name}' registered successfully.")

    def search_properties(self, search_price=None, search_type=None):
        found_properties = [p for p in self.properties if (search_price is None or p.price <= search_price) and (search_type is None or p.type_ == search_type)]
        if found_properties:
            for property in found_properties:
                print(property)
        else:
            print("No matching properties found.")

    def make_transaction(self, buyer, property_id):
        # Find the property
        property_to_sell = next((p for p in self.properties if p.property_id == property_id and p.status == 'Available'), None)
        
        if property_to_sell:
            if buyer.role != 'Buyer':
                print(f"Only buyers can make transactions. {buyer.name} is a {buyer.role}.")
            else:
                # Perform transaction
                property_to_sell.status = 'Sold'
                self.transactions.append((buyer, property_to_sell))
                print(f"Transaction completed: {buyer.name} bought {property_to_sell.address}.")

        else:
            print("Property not found or already sold.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions made yet.")
        else:
            for buyer, property in self.transactions:
                print(f"{buyer.name} bought {property.address} for {property.price}.")

# Step 2: Example usage
if __name__ == "__main__":
    system = RealEstateSystem()

    # Register users
    system.register_user("Alice", "Seller")
    system.register_user("Bob", "Buyer")
    system.register_user("Charlie", "Agent")

    # Add properties
    system.add_property("123 Main St", 250000, "House", "Alice")
    system.add_property("456 Elm St", 150000, "Condo", "Alice")
    system.add_property("789 Oak St", 350000, "House", "Alice")

    # List all properties
    print("\nAvailable Properties:")
    system.list_properties()

    # Search for properties based on price or type
    print("\nSearch Results (Price <= 200000):")
    system.search_properties(search_price=200000)

    print("\nSearch Results (Type = House):")
    system.search_properties(search_type="House")

    # Make a transaction
    buyer = next(user for user in system.users if user.name == "Bob")
    system.make_transaction(buyer, 1)

    # View transactions
    print("\nTransaction History:")
    system.view_transactions()

    # View updated property list
    print("\nUpdated Property List:")
    system.list_properties()
