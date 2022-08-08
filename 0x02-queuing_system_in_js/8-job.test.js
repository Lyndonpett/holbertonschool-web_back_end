import createPushNotificationsJobs from './8-job.js';
const kue = require('kue');
const queue = kue.createQueue();
const expect = require('chai').expect;

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.exit();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  it('should test non array input', () => {
    expect(() => createPushNotificationsJobs('string', queue)).to.throw(
      Error,
      'Jobs is not an array'
    );
    expect(() => createPushNotificationsJobs(NaN, queue)).to.throw(
      Error,
      'Jobs is not an array'
    );
    expect(() => createPushNotificationsJobs({ k: 'v' }, queue)).to.throw(
      Error,
      'Jobs is not an array'
    );
  });

  it('should test creating jobs for queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queue.testMode.jobs[0].data.message).to.equal(
      'This is the code 1234 to verify your account'
    );
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('4153518781');
    expect(queue.testMode.jobs[1].data.message).to.equal(
      'This is the code 4562 to verify your account'
    );
  });
});
