export default function getStudentIdsSum(listOfStudents) {
  return listOfStudents.reduce(
    (previousValue, currentValue) => previousValue + currentValue.id,
    0,
  );
}
