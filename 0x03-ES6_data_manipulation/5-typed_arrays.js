export default function createInt8TypedArray(length, position, value) {
  if (position > length || position < 0) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const array = new Int8Array(buffer);

  for (let i = 0; i < length; i += 1) {
    if (i === position) {
      array[i] = value;
    }
  }
  return new DataView(buffer);
}
