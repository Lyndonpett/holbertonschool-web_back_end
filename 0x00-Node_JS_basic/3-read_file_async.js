// reads a file asynchronously
const fs = require('fs');

const countStudents = async (file) => {
  let content;
  try {
    content = await fs.promises.readFile(file, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  let lines = content.split('\n');
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const field = lines.map((line) => line.split(',')[3]);
  const eachField = [...new Set(field)];

  const dict = {};

  for (let i = 0; i < eachField.length; i += 1) {
    const numStudents = field.filter(
      (fieldName) => fieldName === eachField[i],
    ).length;

    const studentsPerField = lines.filter(
      (line) => line.split(',')[3] === eachField[i],
    );

    const names = studentsPerField.map((line) => line.split(',')[0]);

    console.log(
      `Number of students in ${
        eachField[i]
      }: ${numStudents}. List: ${names.join(', ')}`,
    );

    dict[eachField[i]] = {
      numStudents,
      names,
    };
  }
  return dict;
};

module.exports = countStudents;
