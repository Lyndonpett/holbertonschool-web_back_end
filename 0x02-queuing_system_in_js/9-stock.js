const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
    currentQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
    currentQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
    currentQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
    currentQuantity: 5,
  },
];

const getItemById = (itemId) => {
  return listProducts.find((item) => item.itemId === itemId);
};

const express = require('express');
const app = express();

app.listen('1245');

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

const redis = require('redis');
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Write a function reserveStockById that will take itemId and stock as arguments:
// It will set in Redis the stock for the key item.ITEM_ID

const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Write an async function getCurrentReservedStockById, that will take itemId as an argument:
// It will return the reserved stock for a specific item

const getCurrentReservedStockById = async (itemId) => {
  await getAsync(`item.${itemId}`);
};

//Create the route GET /list_products/:itemId, that will return the current product and the current available stock (by using getCurrentReservedStockById)
app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (item) {
    getCurrentReservedStockById(itemId).then(() => {
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
    return res.status(404).send({ status: 'Product not found' });
  }
  if (item.currentQuantity <= 0) {
    res.status(400).send({ status: 'Not enough stock' });
  } else {
    item.currentQuantity--;
    reserveStockById(itemId, item.currentQuantity);
    res.send({ status: 'Reservation confirmed', itemId: itemId });
  }
});
