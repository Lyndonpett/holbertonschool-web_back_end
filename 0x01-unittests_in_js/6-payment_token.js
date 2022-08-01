// on success return true, otherwise do nothing
const getPaymentTokenFromAPI = (success) => {
  if (success) {
    return new Promise((resolve, reject) => {
      resolve({ data: 'Successful response from the API' });
    });
  }
};

modules.export = getPaymentTokenFromAPI;
