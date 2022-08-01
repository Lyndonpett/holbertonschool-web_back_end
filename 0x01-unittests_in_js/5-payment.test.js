const sendPaymentRequestToApi = require('./5-payment');
const sinon = require('sinon');
const { expect } = require('chai');

describe('sendPaymentRequestToApi', () => {
  let spyFunction;

  beforeEach(() => {
    spyFunction = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyFunction.restore();
  });

  it('Test sendPaymentRequestToApi logs 120', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spyFunction.calledWith('The total is: 120')).to.be.true;
    expect(spyFunction.calledOnce).to.be.true;
  });

  it('Test sendPaymentRequestToApi logs 20', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spyFunction.calledWith('The total is: 20')).to.be.true;
    expect(spyFunction.calledOnce).to.be.true;
  });
});
