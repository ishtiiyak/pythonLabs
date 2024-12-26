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


# Example usage
package1 = Package("Ahmad", "110", "City", "State", "ZIPcodeSender", "ZIPcodeReceiver", 12, 3)
print("Package1 Cost:", package1.calculate_cost())

package2 = TwoDayPackage("Ali", "2201", "City", "State", "ZIPcodeSender", "ZIPcodeReceiver", 6, 7, 5)
print("TwoDayPackage Cost:", package2.calculate_cost())

package3 = OvernightPackage("Sara", "110", "City", "State", "ZIPcodeSender", "ZIPcodeReceiver", 8, 4, 2)
print("OvernightPackage Cost:", package3.calculate_cost())
