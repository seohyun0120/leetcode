/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    let size = sandwiches.legnth;
    let cnt = 0;
    
    while (sandwiches.length) {
        // 샌드위치 먹음
        if (students[0] === sandwiches[0]) {
            students.shift();
            sandwiches.shift();
            cnt = 0;
        } else {
            // 못먹음
            if (cnt === sandwiches.length) {
                // 전부 못먹음
                break;
            }
            // 못 먹은 학생 뒤로 보내고 숫자 셈
            students.push(students.shift());
            cnt++;
        }
    }
    
    return students.length;
};