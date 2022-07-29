const calculateNumber = require('./1-calcul.js');
const assert = require('assert').strict;

describe('calculateNumber', () => {
  it('taking in postive num and return the result', () => {
    assert.equal(calculateNumber('SUM', 1, 2), 3);
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.equal(calculateNumber('DIVIDE', 1.5, 2), 1);
  });

  it('taking in negative nums and return the result', () => {
    assert.equal(calculateNumber('SUM', 1, -2), -1);
    assert.equal(calculateNumber('SUBTRACT', -1.4, 4.5), -6);
    assert.equal(calculateNumber('DIVIDE', -1.5, 2), -0.5);
  });

  it('taking in a 0 while dividing', () => {
    assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
});
