/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    let nh = [];
    
    for (let i=0; i<names.length; i++) {
        nh.push([names[i], heights[i]]);
    }

    nh.sort((a, b) => b[1] - a[1]);

    let ans = [];
    for (let i=0; i<nh.length; i++) {
        ans.push(nh[i][0]);
    }
    
    return ans;
};