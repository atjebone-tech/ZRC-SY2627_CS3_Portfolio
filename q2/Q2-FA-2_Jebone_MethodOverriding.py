class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        discount = self.get_bill_amount() * 0.20
        return self.get_bill_amount() - discount

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        discount = self.get_bill_amount() * 0.15
        return self.get_bill_amount() - discount


regular = Patient("Ana Cruz", 20000)
senior = SeniorPatient("Jose Reyes", 20000)
philhealth = PhilHealthPatient("Carlo Garcia", 20000)

patient_list = [regular, senior, philhealth]

for patient in patient_list:
    print("Patient Name:", patient.get_name())
    print("Original Bill: ₱{:,.2f}".format(
        patient.get_bill_amount()
    ))
    print("Final Bill: ₱{:,.2f}".format(
        patient.calculate_bill()
    ))
    print("-" * 35)