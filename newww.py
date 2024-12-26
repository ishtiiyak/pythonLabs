










#class



class Package():
    def __init__(self,name,adress,city,state,ZIPcodeSender,ZIPcodeReceiver,weight,cost_per_ounce):
        self.name=name
        self.adress=adress
        self.city=city
        self.state=state
        self.ZIPcodeSender=ZIPcodeSender
        self.ZIPcodeReceiver=ZIPcodeReceiver
        self.weight=abs(weight)
        self.cost_per_ounce=abs(cost_per_ounce)



class Package():
    def __init__(self,name,adress,city,state,ZIPcodeSender,ZIPcodeReceiver,weight,cost_per_ounce):
        self.name=name
        self.adress=adress
        self.city=city
        self.state=state
        self.ZIPcodeSe=ZIPcodeSender
        self.ZIPcodeRe=ZIPcodeReceiver
        self.weight=abs(weight)
        self.cost_per_ounce=abs(cost_per_ounce)
    def cost(self):
        return self.weight*self.cost_per_ounce

class TwoDayPackage(Package):
    def __init__(self,name,adress,city,state,ZIPcodeSender,ZIPcodeReceiver,weight,cost_per_ounce):
       su
    

class OvernightPackage(Package):
    def __init__(self,name,adress,city,state,ZIPcode,flatfee):
        self.name=name
        self.adress=adress
        self.city=city
        self.state=state
        self.ZIPcode=ZIPcode
        self.flatfee=flatfee
    

package1=Package("name","address","city","state","ZIPcodeSender","ZIPcodeReceiver",12,3)
print(package1.weight)
print(package1.cost_per_ounce)

package2=TwoDayPackage("name","address","city","state","ZIPcodeSender","ZIPcodeReceiver",6,7)
print(package2.weight)
package3=OvernightPackage("name","address","city","state","ZIPcode",10)
