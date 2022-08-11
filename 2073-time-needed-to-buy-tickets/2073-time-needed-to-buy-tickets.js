/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function(tickets, k) {
    // 한 번 살 때 하나의 티켓만 살 수 있음
    // 티켓을 다 샀으면 줄을 더이상 서지않아도 됨

    let cnt = 0;
    
    while (tickets[k] > 0) {
        for (let i=0; i<tickets.length; i++) {
            if (tickets[i] > 0) {
                tickets[i]--;
                cnt++;
            }

            if (tickets[k] === 0) return cnt;            
        }
    }
};