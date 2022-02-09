export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }

  const newArray = [];

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      newArray.push(value.slice(startString.length));
    }
  }
  return newArray.join('-');
}
