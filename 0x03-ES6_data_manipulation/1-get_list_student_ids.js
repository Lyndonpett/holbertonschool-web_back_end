export default function getListStudentIds(array) {
  if (array instanceof Array) {
    return array.map((student) => student.id);
  }
  return [];
}
