class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        self.speed += m * 10
        return self.speed

    def brake(self, n):
        reduction = n * 10
        self.speed = max(0, self.speed - reduction)
        return self.speed


class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=0):
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self):
        self.battery = min(100, self.battery + 20)
        return self.battery


# 测试代码
if __name__ == "__main__":
    car = Car("Toyota")
    car.accelerate(3)
    print(f"当前速度: {car.speed}")  # 输出 30
    car.brake(2)
    print(f"刹车后的速度: {car.speed}")  # 输出 10

    e_car = ElectricCar("Tesla", 20, 60)
    e_car.accelerate(2)
    print(f"电动车当前速度: {e_car.speed}")  # 输出 40
    e_car.charge()
    print(f"充电后的电量: {e_car.battery}")  # 输出 80