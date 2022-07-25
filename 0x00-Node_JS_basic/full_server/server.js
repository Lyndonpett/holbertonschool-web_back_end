// sets up server used in other files
import express from 'express';

const routes = require('./routes/index');

const app = express();

app.use(routes);

app.listen(1245);

export default app;
