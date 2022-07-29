const calculateNumber = require('./1-calcul.js');
const expect = require('chai').expect;

describe('calculateNumber', () => {
  it('taking in postive num and return the result', () => {
    expect(calculateNumber('SUM', 1, 2)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    expect(calculateNumber('DIVIDE', 1.5, 2)).to.equal(1);
  });

  it('taking in negative nums and return the result', () => {
    expect(calculateNumber('SUM', 1, -2)).to.equal(-1);
    expect(calculateNumber('SUBTRACT', -1.4, 4.5)).to.equal(-6);
    expect(calculateNumber('DIVIDE', -1.5, 2)).to.equal(-0.5);
  });

  it('taking in a 0 while dividing', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
  });
});
