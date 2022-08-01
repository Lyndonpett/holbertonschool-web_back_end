const getPaymentTokenFromAPI = require('./6-payment_token');
const expect = require('chai').expect;

describe('getPaymentTokenFromAPI', () => {
  it('Tests that a new promise is returned', (done) => {
    const result = getPaymentTokenFromAPI(true);
    expect(result).to.be.an.instanceof(Promise);
    done();
  });
});
