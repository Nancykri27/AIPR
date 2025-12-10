const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function printStudents(students) {
    console.log("Student List:");
    students.forEach(student => {
        console.log(student);
    });
}

rl.question('Enter student names separated by commas: ', (input) => {
    const studentNames = input.split(',').map(name => name.trim());
    printStudents(studentNames);
    rl.close();
});