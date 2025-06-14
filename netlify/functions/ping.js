const fetch = require('node-fetch');

exports.handler = async function() {
  try {
    const res = await fetch('http://136.243.69.23', { method: 'HEAD', timeout: 3000 });
    if (res.ok) {
      return {
        statusCode: 200,
        body: 'OK'
      };
    } else {
      return {
        statusCode: 500,
        body: 'DOWN'
      };
    }
  } catch (err) {
    return {
      statusCode: 500,
      body: 'DOWN'
    };
  }
};
