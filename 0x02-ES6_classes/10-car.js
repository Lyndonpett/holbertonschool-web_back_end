export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // have to assign, create, then get prototype
    return Object.assign(Object.create(Object.getPrototypeOf(this)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
