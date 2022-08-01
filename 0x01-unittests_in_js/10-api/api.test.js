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

  it('Tests /cart/:id is working', (done) => {
    request('http://localhost:7865/cart/1', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 1');
      done();
    });
  });

  it('Tests /cart/:id fails when given non-number', (done) => {
    request('http://localhost:7865/cart/a', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('Tests /available_payments returns correct code and results', (done) => {
    request(
      'http://localhost:7865/available_payments',
      (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal(
          '{"payment_methods":{"credit_cards":true,"paypal":false}}'
        );
        done();
      }
    );
  });

  it('Tests POST /login returns correct code and results', (done) => {
    request({
        method: 'POST',
        uri: 'http://localhost:7865/login',
        json: {
          userName: 'John'
        }
      },
      (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome John');
        done();
      }
    );
  });
});
