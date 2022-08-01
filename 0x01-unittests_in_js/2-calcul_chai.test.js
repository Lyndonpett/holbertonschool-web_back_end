const calculateNumber = require('./1-calcul.js');
const expect = require('chai').expect;

describe('calculateNumber', () => {
  it('taking in postive num and return the result', () => {
    expect(calculateNumber('SUM', 1, 2)).to.be.eq(3);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.be.eq(-4);
    expect(calculateNumber('DIVIDE', 1.5, 2)).to.be.eq(1);
  });

  it('taking in negative nums and return the result', () => {
    expect(calculateNumber('SUM', 1, -2)).to.be.eq(-1);
    expect(calculateNumber('SUBTRACT', -1.4, 4.5)).to.be.eq(-6);
    expect(calculateNumber('DIVIDE', -1.5, 2)).to.be.eq(-0.5);
  });

  it('taking in a 0 while dividing', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.be.eq('Error');
  });

  it('taking in type SUM', () => {
    expect(calculateNumber('SUM', 1, 2)).to.be.eq(3);
    expect(calculateNumber('SUM', 2, 5)).to.be.eq(7);
    expect(calculateNumber('SUM', 4, -5)).to.be.eq(-1);
    expect(calculateNumber('SUM', 3, 2)).to.be.eq(5);
    expect(calculateNumber('SUM', -2, -5)).to.be.eq(-7);
  });
});
