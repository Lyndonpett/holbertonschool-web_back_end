// connect to redis server and log a message for status

const redis = require('redis');
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
  });

const updateCache = (key, value) => {
  client.hset('HolbertonSchools', key, value, redis.print);
};

const getCache = () => {
  client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) {
      console.log(err);
    } else {
      console.log(obj);
    }
  });
};

updateCache('Portland', '50');
updateCache('Seattle', '80');
updateCache('New York', '20');
updateCache('Bogota', '20');
updateCache('Cali', '40');
updateCache('Paris', '2');
getCache();
