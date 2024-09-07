class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        result = self.__cpu * self.__memory
        return f"Результат вычислений: {result}"

    def __str__(self):
        return f"Computer with CPU: {self.__cpu} and Memory: {self.__memory} GB"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Phone with SIM cards: {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone with CPU: {self.cpu}, Memory: {self.memory} GB, SIM cards: {', '.join(self.sim_cards_list)}"


computer = Computer(3.5, 16)
phone = Phone(["Beeline", "O!"])
smartphone1 = SmartPhone(2.5, 8, ["MegaCom", "Beeline"])
smartphone2 = SmartPhone(3.0, 16, ["O!", "MegaCom"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)



print(computer.make_computations())
print(computer == smartphone1)
print(computer > smartphone1)

phone.call(1, "+996 777 99 88 11")
phone.call(2, "+996 555 12 34 56")

smartphone1.use_gps("Центр города")
smartphone1.call(1, "+996 777 77 77 77")
print(smartphone1.make_computations())
