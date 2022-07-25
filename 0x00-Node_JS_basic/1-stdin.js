// asks name of user and prints it

console.log('Welcome to Holberton School, what is your name?');

process.stdin
  .on('readable', () => {
    const name = process.stdin.read();
    if (name) {
      console.log(`Your name is: ${name}`);
    }
  })

.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
