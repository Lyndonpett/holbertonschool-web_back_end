// attempt to read the database file synchronously

const fs = require('fs');

const countStudents = (file) => {
  if (!fs.existsSync(file)) {
    throw new Error('Cannot load the database');
  }

  const students = fs.readFileSync(file, 'utf8');
  let lines = students.split('\n');

  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const field = lines.map((line) => line.split(',')[3]);

  const eachField = [...new Set(field)];

  eachField.forEach((fieldName) => {
    const studentsPerField = lines
      .filter((line) => line.endsWith(fieldName))
      .map((line) => {
        const split = line.split(',');
        return split[0];
      });
    console.log(
      `Number of students in ${fieldName}: ${
        studentsPerField.length
      }. List: ${studentsPerField.join(', ')}`
    );
  });
};

module.exports = countStudents;
