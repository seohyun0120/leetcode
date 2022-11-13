/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    let res = [];
    for (let i=0; i<image.length; i++) {
        let a = image[i];
        a.reverse();
        a = a.map(x => 1-x);
        res.push(a);
    }
    
    return res;
};