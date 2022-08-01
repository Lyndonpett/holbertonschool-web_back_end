// Utils module

const Utils = {
  calculateNumber(type, a, b) {
    const whichType = type.toLowerCase();
    if (isNaN(a) || isNaN(b)) throw new TypeError('Arguments must be numbers');

    switch (whichType) {
      case 'sum':
        return Math.round(a) + Math.round(b);
      case 'subtract':
        return Math.round(a) - Math.round(b);
      case 'divide':
        if (Math.round(b) === 0) return 'Error';
        return Math.round(a) / Math.round(b);
      default:
        throw new TypeError('Arguments must be SUM, SUBTRACT or DIVIDE');
    }
  }
};

module.exports = Utils;
