const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 10,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const getItemById = (id) => {
  return listProducts.find((item) => item.itemId === id);
};

const express = require('express');
const app = express();

app.listen(1245);

app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

const redis = require('redis');
const client = redis.createClient();
const { promisify } = require('util');

const reserveStockById = (itemId, stock) => {
  const asyncSet = promisify(client.set).bind(client);
  asyncSet(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const asyncGet = promisify(client.get).bind(client);
  await asyncGet(`item.${itemId}`);
};

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (item) {
    getCurrentReservedStockById(itemId).then((stock) => {
      item.initialAvailableQuantity = stock;
      res.send(item);
    });
  } else {
    res.status(404).send({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));

  if (!item) {
    res.status(404).send({ status: 'Product not found' });
  }

  if (item.initialAvailableQuantity <= 0) {
    res.status(404).send({ status: 'Product not available' });
  } else {
    getCurrentReservedStockById(itemId).then((stock) => {
      const newStock = stock - 1;
      reserveStockById(itemId, newStock);
      res.send({ status: 'Reservation confirmed', itemId: itemId });
    });
  }
});
