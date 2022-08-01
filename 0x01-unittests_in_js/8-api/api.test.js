const { expect } = require('chai');
const request = require('request');

describe('API Test', () => {
  it('Tests that GET returns correct code and results', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
