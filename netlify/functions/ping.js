const { exec } = require('child_process');

exports.handler = async function(event, context) {
  return new Promise((resolve, reject) => {
    exec('ping -c 1 136.243.69.23/login', (error) => {
      if (error) {
        resolve({ statusCode: 500, body: 'DOWN' });
      } else {
        resolve({ statusCode: 200, body: 'OK' });
      }
    });
  });
};
