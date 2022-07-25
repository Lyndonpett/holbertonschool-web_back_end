// Create a more complex HTTP server using Node's HTTP module
const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http
  .createServer(async (req, res) => {
    if (req.url === '/') {
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
      res.write('This is the list of our students\n');

      await countStudents(process.argv[2])
        .then((data) => {
          const fields = Object.keys(data);

          const total = fields.reduce(
            (acc, curr) => acc + data[curr].numStudents,
            0,
          );

          res.write(`Number of students: ${total}\n`);

          for (let i = 0; i < fields.length; i += 1) {
            res.write(
              `Number of students in ${fields[i]}: ${
                data[fields[i]].numStudents
              }. `,
            );
            res.write(`List: ${data[fields[i]].names.join(', ')}`);

            if (i < fields.length - 1) {
              res.write('\n');
            }
          }
        })
        .catch((err) => {
          res.write(err.message);
        })
        .finally(() => {
          res.end();
        });
    }
  })
  .listen(1245);

module.exports = app;
