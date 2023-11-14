import matplotlib.pyplot as plt

class PressureVolumeDiagram:
    def __init__(self):
        # Initialize instance variables
        self.points_qnt = 0
        self.points = []
        self.total_work = 0

    def inputData(self):
        # Collect input data from the user
        self.points_qnt = int(input("Input the points quantity: "))
        for i in range(1, self.points_qnt + 1):
            pressure = float(input("Input the pressure(atm) at point " + str(i) + ": "))
            volume = float(input("Input the volume(L) at point " + str(i) + ": "))
            self.points.append({"pressure": pressure, "volume": volume})

    def calculate(self):
        w = 0

        # Calculate the work done during the process
        for i in range(1, len(self.points)):
            # Calculate the change in volume
            dV = self.points[i]['volume'] - self.points[i - 1]['volume']
            # Calculate the change in work
            dW = self.points[i]['pressure'] * (dV)

            # Update the total work
            w += dW

        self.total_work = w

    def view(self):
        # Convert total work from atm·L to joules and display the result
        work = self.total_work * 101.325
        print(f"Work (J): {work}")

    def start(self):
        # Execute the complete process
        self.inputData()
        self.calculate()
        self.view()

# Create an instance of PressureVolumeDiagram
pvd = PressureVolumeDiagram()

# Start the analysis process
pvd.start()
