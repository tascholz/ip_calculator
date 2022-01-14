import sys

class Ip:
    def __init__(self, adress):
        self.adress = adress
    
    @classmethod
    def fromString(cls, adress):
        adress_list = adress.split(".")
        for i in range(len(adress_list)):
            adress_list[i] = int(adress_list[i])
        return cls(adress_list)

    def adress_to_binary_string(self):
        adress = [0, 0, 0, 0]
        for i in range(len(adress)):
            adress[i] = str(bin(self.adress[i]))[2:].zfill(8)
        return adress

    def show(self):
        return str(self.adress[0]) + "." + str(self.adress[1]) + "." + str(self.adress[2]) + "." + str(self.adress[3])

class Calculator:
    def __init__(self, ip_adress):
        self.ip, self.suffix = ip_adress.split("/")
        self.ip = Ip.fromString(self.ip)

    def calculate_subnet_mask(self):
        mask = [255, 255, 255, 255]
        suffix = 32 - int(self.suffix)

        for i in range(suffix):
            if i <= 7:
                mask[3] -= 2**(i)
            if i <=15 and i > 7:
                mask[2] -= 2**(i-8)
            if i <=23 and i > 15:
                mask[1] -= 2**(i-16)
            if i > 23:
                mask[0] -= 2**(i-24)
        return Ip(mask)
        
    def calculate_number_of_hosts(self):
        hosts = 255 - self.calculate_subnet_mask().adress[3]
        hosts += (255 - self.calculate_subnet_mask().adress[2]) * 2 **8
        hosts += (255 - self.calculate_subnet_mask().adress[1]) * 2 **16
        hosts += (255 - self.calculate_subnet_mask().adress[0]) * 2 **24
        hosts -= 1
        return str(hosts)
        
    def calculate_network_adress(self):
        network_adress = [0, 0, 0, 0]
        for i in range(len(network_adress)):
            network_adress[i] = self.calculate_subnet_mask().adress[i] & self.ip.adress[i]
        return Ip(network_adress)

    def calculate_first_host(self):
        host_ip = [0, 0, 0, 0]
        for i in range(len(host_ip)):
            host_ip[i] = self.calculate_network_adress().adress[i]
        host_ip[3] += 1
        return Ip(host_ip)

    def calculate_last_host(self):
        last_host = [0, 0, 0, 0]
        for i in range (len(last_host)):
            subnet_mask_octett = list(self.calculate_subnet_mask().adress_to_binary_string()[i])
            network_adress_octett = list(self.calculate_network_adress().adress_to_binary_string()[i])

            for j in range(len(subnet_mask_octett)):
                if subnet_mask_octett[j] == "0":
                    network_adress_octett[j] = "1"\

            last_host[i] = "".join(network_adress_octett)
            last_host[i] = int(last_host[i], base=2)
        
        last_host[3] -= 1
        return Ip(last_host)


    def show(self):
        print("")
        print("############### IP Calculator ###############")
        table_data = [
            ["IP adress:", self.ip.show()],
            ["Subnet mask:", self.calculate_subnet_mask().show()],
            ["Number of hosts:", self.calculate_number_of_hosts()],
            ["Network adress:", self.calculate_network_adress().show()],
            ["First host:", self.calculate_first_host().show()],
            ["Last host:", self.calculate_last_host().show()]
        ]

        for row in table_data:
            print("{: >20} {: >20}".format(*row))
        print("")
        

def calculate_network(ip):
    ip_calc = Calculator(ip)
    ip_calc.show()
    pass

if __name__ == '__main__':
    ip = sys.argv[1]
    calculate_network(ip)
