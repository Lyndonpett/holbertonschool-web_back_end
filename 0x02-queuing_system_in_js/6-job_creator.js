// Create a queue with Kue and create object with job data
const kue = require('kue');
const queue = kue.createQueue();

const job = queue
  .create('push_notification_code', {
    phoneNumber: '+1-212-555-1212',
    message: 'Hello World!',
  })
  .save();

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });
