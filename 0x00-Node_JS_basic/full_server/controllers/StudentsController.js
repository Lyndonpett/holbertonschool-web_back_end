// controller for ui for /students route
import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    res.status(200);
    readDatabase(process.argv[2])
      .then((data) => {
        res.write('This is the list of our students\n');

        const fields = Object.keys(data);

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

  static getAllStudentsByMajor(req, res) {
    res.status(200);
    readDatabase(process.argv[2])
      .then((data) => {
        const fields = Object.keys(data);

        const { major } = req.params;

        if (fields.includes(major)) {
          res.write(`List: ${data[major].names.join(', ')}`);
        } else {
          res.status(500);
          res.write('Major parameter must be CS or SWE');
        }
      })
      .catch((err) => {
        res.write(err.message);
      })
      .finally(() => {
        res.end();
      });
  }
}

module.exports = StudentsController;
