// read the database asynchronously and returns a promise
import countStudents from '../3-read_file_async';

const readDatabase = (path) => countStudents(path);

module.exports = readDatabase;
