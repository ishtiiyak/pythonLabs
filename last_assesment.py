class Package:
    def __init__(self, name, address, city, state, ZIPcodeSender, ZIPcodeReceiver, weight, cost_per_ounce):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.ZIPcodeSender = ZIPcodeSender
        self.ZIPcodeReceiver = ZIPcodeReceiver
        self.weight = abs(weight)
        self.cost_per_ounce = abs(cost_per_ounce)

    def calculate_cost(self):
        return self.weight * self.cost_per_ounce


class TwoDayPackage(Package):
    def __init__(self, name, address, city, state, ZIPcodeSender, ZIPcodeReceiver, weight, cost_per_ounce, flat_fee):
        super().__init__(name, address, city, state, ZIPcodeSender, ZIPcodeReceiver, weight, cost_per_ounce)
        self.flat_fee = abs(flat_fee)

    def calculate_cost(self):
        return super().calculate_cost() + self.flat_fee


class OvernightPackage(Package):
    def __init__(self, name, address, city, state, ZIPcodeSender, ZIPcodeReceiver, weight, cost_per_ounce, fee_per_ounce):
        super().__init__(name, address, city, state, ZIPcodeSender, ZIPcodeReceiver, weight, cost_per_ounce)
        self.fee_per_ounce = abs(fee_per_ounce)

    def calculate_cost(self):
        return self.weight * (self.cost_per_ounce + self.fee_per_ounce)


package1 = Package("Ahmad", "110", "Lahore", "Punjab", "5001", "1200", 12, 3)
print("Package1 Cost:", package1.calculate_cost())
print(f"City: {package1.city}, State: {package1.state}, ZIP: {package1.ZIPcodeSender} -> {package1.ZIPcodeReceiver}")

package2 = TwoDayPackage("Ali", "2201", "Karachi", "Sindh", "8000", "9000", 6, 7, 5)
print("TwoDayPackage Cost:", package2.calculate_cost())
print(f"City: {package2.city}, State: {package2.state}, ZIP: {package2.ZIPcodeSender} -> {package2.ZIPcodeReceiver}")

package3 = OvernightPackage("Sara", "110", "Nagar", "GB", "12000", "5000", 8, 4, 2)
print("OvernightPackage Cost:", package3.calculate_cost())
print(f"City: {package3.city}, State: {package3.state}, ZIP: {package3.ZIPcodeSender} -> {package3.ZIPcodeReceiver}")
