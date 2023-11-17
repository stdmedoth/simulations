import matplotlib.pyplot as plt

class IdealGasLaw:
    def __init__(self):
        pass

    def initialize(self, pressure=1, temperature=1, volume=1):
        self.temperature = []
        self.pressure = []
        self.volume = []
        self.work = [0]
        self.int_energy = [0]
        self.time = [0]
        self.dV = 0.01
        self.dP = 0.01
        self.dT = 0.01
        self.n = 0.32
        self.R = 4.314

        self.set_temperature(temperature)
        self.set_pressure(volume)
        self.set_volume(volume)

    def set_temperature(self, temperature):
        self.temperature.append(temperature)

    def set_volume(self, volume):
        self.volume.append(volume)

    def set_pressure(self, pressure):
        self.pressure.append(pressure)

    def set_temperature_constant_pressure(self, temperature):
        actual_temp = self.temperature[-1:]
        actual_temp = actual_temp.pop()


        dtemp = abs(temperature - actual_temp)
        for i in range(int(dtemp/self.dV)):

            iT = self.temperature[i] + self.dT
            self.temperature.append(iT)
        
            self.pressure.append(self.pressure[i])
            
            dV = (self.n * self.R * self.dT)/self.pressure[i]
            iV = self.volume[i] + dV
            self.volume.append(iV)

    def set_temperature_constant_volume(self, temperature):
        actual_temp = self.temperature[-1:]
        actual_temp = actual_temp.pop()


        dtemp = abs(temperature - actual_temp)
        for i in range(int(dtemp/self.dV)):

            iT = self.temperature[i] + self.dT
            self.temperature.append(iT)
        
            self.volume.append(self.volume[i])
            
            dP = (self.n * self.R * self.dT)/self.volume[i]
            iP = self.pressure[i] + dP
            self.pressure.append(iP)

    
    def view(self):
        pass

    def igraph(self, y):
        fig = plt.figure()
        ax = fig.add_subplot()

        

        if y == 'volume':
            ax.scatter(self.volume, self.temperature)
        if y == 'pressure':
            ax.scatter(self.pressure, self.temperature)

        plt.show()

    def start(self):
        self.initialize()

        self.initialize(pressure=2.4, volume=2.2)
        self.set_temperature_constant_pressure(402)
        #self.set_temperature_constant_volume(201)

        self.igraph(y='volume') # y = 'volume|pressure'
    

isys = IdealGasLaw()
isys.start()