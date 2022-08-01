const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');
const expect = require('chai').expect;
const sinon = require('sinon');

describe('sendPaymentRequestToApi', () => {
  it('Make sure math for sendPaymentRequestToAPI is the same as calculateNumber', () => {
    const spiedFunction = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spiedFunction.calledWith('SUM', 100, 20)).to.be.true;
    spiedFunction.restore();
  });

  it('Using stub to test sendPaymentRequestToApi is correct', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spyFunction = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(spyFunction.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    spyFunction.restore();
  });
});
