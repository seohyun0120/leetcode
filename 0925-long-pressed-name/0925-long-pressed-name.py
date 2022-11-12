class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            # 현재 인덱스의 name, typed 알파벳이 같으면 넘어감
            if i < len(name) and name[i] == typed[j]:
                i += 1
            # typed의 j, j-1 index가 다르면 false
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)