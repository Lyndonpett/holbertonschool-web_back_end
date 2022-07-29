const calculateNumber = require('./0-calcul.js');
const assert = require('assert').strict;

describe('calculateNumber', () => {
  it('taking in postive num and return the sum', () => {
    assert.equal(calculateNumber(1, 2), 3);
    assert.equal(calculateNumber(1.5, 2.5), 5);
    assert.equal(calculateNumber(1.5, 2), 4);
    assert.equal(calculateNumber(1, 2.5), 4);
  });

  it('taking in negative nums and return the sum', () => {
    assert.equal(calculateNumber(-1, -2), -3);
    assert.equal(calculateNumber(-1.5, -2.5), -3);
    assert.equal(calculateNumber(-1.5, -2), -3);
    assert.equal(calculateNumber(-1, -2.5), -3);
  });

  it('taking in NaN and return the sum', () => {
    assert.throws(() => calculateNumber(1, 'a'), TypeError);
    assert.throws(() => calculateNumber(NaN, 2), TypeError);
  });
});
