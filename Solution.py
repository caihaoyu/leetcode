# -*- coding: utf-8 -*-
def twoSum(nums, target):
    """
    :type nums: nums[int]
    :type target: int
    :rtype: nums[int]
    """
    check = {}
    for i,num in enumerate(nums):
        if num not in check:
            check[target-num]=i
        else:
            return [min(i,check[num]),max(i,check[num])]

def isPalindrome(s):
    return s == s[::-1]


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        def getList(list):
            result = []
            if list.next == None:
                result.append(list.val)
            while list.next != None:
                result.append(list.val)
                list = list.next
                if list.next == None:
                    result.append(list.val)
            return result
        def getNumber(list):
            result = ''
            for i in range(len(list)):
                index = len(list)-1-i
                result += str(list[index])
            return int(result)
        l1 = getList(l1)
        l2 = getList(l2)
        sum = getNumber(l1) + getNumber(l2)
        n = str(sum)
        temp = None
        for i in range(len(n)):
            index = len(n)-1 - i
            if result == None:
                result = ListNode(int(n[index]))
            else:
                if temp == None:
                    temp = ListNode(int(n[index]))
                    temp2 = temp
                else:
                    temp1 = ListNode(int(n[index]))
                    temp2.next = temp1
                    temp2 = temp1
        result.next = temp
        return result
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        dict = {}
        start = 0
        for i,c in enumerate(s):
            # restart or end
            if c not in dict or dict[c] < start:
                r = max(r,i - start + 1)
            else:
                # if zero
                start = dict[c]+1
            dict[c] = i
        return r
    def findMedianSortedArrays(self, nums1, nums2):
        sum = len(nums1) + len(nums2)
        left = 0
        right = 0
        res = []
        while True:
            if left >= len(nums1):
                res += nums2[right:]
                break
            elif right >= len(nums2):
                res += nums1[left:]
                break
            else:
                if nums1[left] == nums2[right]:
                    res.append(nums1[left])
                    res.append(nums2[right])
                    left += 1
                    right += 1
                elif nums1[left] > nums2[right]:
                    res.append(nums2[right])
                    right += 1
                else:
                    res.append(nums1[left])
                    left += 1
        if len(res) % 2 == 0 :
            return float(res[len(res)/2]+res[len(res)/2-1])/2
        else:
            return float(res[len(res)/2])

    def longestPalindrome(self, s):
        def isPalindrome(str):
            return str == str[::-1]
        if isPalindrome(s):
            return s
        else:
            d = {}
            res = ''
            resIndex = 0
            for i,c in enumerate(s):
                if c in d:
                    d[c].append(i)
                else:
                    d[c] = [i]
            for k,v in d.items():
                if len(v) > 1:
                    start = 0
                    end = len(v)-1
                    index = 0
                    while index < len(v):
                        if v[end]+1 - v[index] > len(res):
                            if isPalindrome(s[v[index]:v[end]+1]):
                                res = s[v[index]:v[end]+1]
                                resIndex = v[index]
                            if index +1 >= end:
                                index += 1
                                end = len(v)-1
                            else:
                                end -= 1
                        elif v[end]+1 - v[index] == len(res) and resIndex > v[index]:
                            if isPalindrome(s[v[index]:v[end]+1]):
                                res = s[v[index]:v[end]+1]
                                resIndex = v[index]
                            if index +1 >= end:
                                index += 1
                                end = len(v)-1
                            else:
                                end -= 1
                        else:
                            index += 1
                            end = len(v)-1

            return res
    def isMatch1(self, s, p):
        def judge(s,p,h=None,index=0):
            c = p[index]
            if h == None:
                h = {}
            last = None
            if h:
                last = h
            history = {}
            if c == '.':
                history = {'type':'.','value':'','isTrue':True,'length':1,'hasWord':False}
                if last:
                    if last["type"] == '*':
                        if last["isTrue"] == True:
                            h = history
                        else:
                            return false
                    elif last["type"] == '.' and last['hasWord'] == False:
                        length = last["length"] + 1
                        history["length"] = length
                        h = history
                    else:
                        history['hasWord'] = True
                        history['value'] = last['value']
                        print last
                        if last["isTrue"] == True:
                            isRight = False
                            length = history["length"]
                            endList = []
                            if last['type'] == '.':
                                length += last['length']+1
                                history["length"] = length
                            if "endList" in last:
                                l = last["endList"]
                            else:
                                l = [n for n in xrange(len(s)) if s.find(history["value"], n) == n]
                            for i in l:
                                end = i+len(history["value"])-1+length
                                # print end
                                if end < len(s):
                                    if s[end] != '\n':
                                        isRight = True
                                        endList.append(end)
                            if isRight:
                                history["endList"] = endList
                                h = history
                            else:
                                # 可能要删除
                                return False
                        else:
                            return False
                else:
                    h = history
            elif c == '*':
                pass
            else:
                history = {'type':'word','value':c,'isTrue':True,'length':1,'hasWord':True,"hasDot":False,"dLength":0}
                history['isTrue'] = c in s
                if last:
                    if last["type"] == ".":
                        history["hasDot"] = True
                        history["dLength"] = last["length"]
                        if history["isTrue"] == True:
                            if last["hasWord"]:
                                isRight = False
                                endList = []
                                for i in last["endList"]:
                                    if i+1 < len(s):
                                        if s[i+1] == c:
                                            isRight = True
                                            endList.append(i+1)
                                if isRight == True:
                                    history["endList"] = endList
                                    h = history
                                else:
                                    return False
                            else:
                                l = [n for n in xrange(len(s)) if s.find(history["value"], n) == n]
                                isRight = False
                                length = 0
                                if last['type'] == '.':
                                    length += last['length']
                                    # history["length"] = length
                                endList = []
                                for i in l :
                                    start = i - length
                                    if start >= 0:
                                        if s[start] != '\n':
                                            isRight = True
                                            endList.append(i)
                                if isRight == True:
                                    history["endList"] = endList
                                    h = history
                                else:
                                    return False
                        else:
                            return False
                    elif last["type"] == "word":
                        history["value"] = last["value"] + c
                        history["isTrue"] = history["value"] in s
                        if last["isTrue"] and last["hasDot"] == False and history["isTrue"] == True:
                            h = history
                        elif last["hasDot"] == True and history["isTrue"] == True:
                            isRight = False
                            endList = []
                            history["hasDot"] = True
                            history["value"] = c
                            for i in last["endList"]:
                                if i+1 < len(s):
                                    if s[i+1] == c:
                                        isRight = True
                                        endList.append(i+1)
                            if isRight == True:
                                history["endList"] = endList
                                h = history
                            else:
                                return False
                        else:
                            return False
                    else:
                        h = history
                else:
                    h = history

            if index+1 < len(p):
                index += 1
                return judge(s,p,h,index)
            else:
                return h["isTrue"]

        if "." in p or "*" in p:
            return judge(s,p)
        else:
            return s == p
    hash = None
    def isMatch(self, s, p,i=0,c=0):
        def check(s,p):
            return p == "." or s == p

        if self.hash == None:
            self.hash = {}
        key = s[i:] + p[c:]
        if key in self.hash:
            return self.hash[key]
        if len(p) <= c:
            if i < len(s):
                return False
            else:
                return True
        elif len(s) <= i:
            c1 = 0
            t = p[c:]
            if len(t) %2 != 0:
                return False
            while c1 < len(t):
                d3 = 0
                if c1+1 < len(t):
                    d3 = t[c1+1]
                if d3 == "*":
                    c1 += 2
                else:
                    return False
            return True
        char = s[i]
        d = p[c]
        d1 = 0
        if len(p) > c+1:
            d1 = p[c+1]
        if d1 == "*":
            if check(char,d):
                self.hash[key] = self.isMatch(s,p,i+1,c) or self.isMatch(s,p,i,c+2)
            else:
                self.hash[key] = self.isMatch(s,p,i,c+2)

        else:
            if check(char,d):
                self.hash[key] = self.isMatch(s,p,i+1,c+1)
            else:
                return False
        return self.hash[key]
    def isMatch2(self, s, p):
        if self.hash is None:
            self.hash = {}
        key = s + p
        if key in self.hash:
            return self.hash[key]

        if p == '':
            return s == ''
        if s == '':
            if len(p) % 2 == 1:
                return False
            i = 1
            while i < len(p):
                if p[i] != '*':
                    return False
                i += 2
            return True

        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            elif p[0] == s[0]:
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                self.hash[key] = self.isMatch(s, p[2:])
        elif p[0] == '.':
            self.hash[key] = self.isMatch(s[1:], p[1:])
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])

        return self.hash[key]




if __name__ == '__main__':
    nums = [3,2,4]
    traget = 6
    print twoSum(nums,traget)
    # l1 = ListNode(0)
    # # node2 = ListNode(4)
    # # node3 = ListNode(3)
    # # node2.next = node3
    # # l1.next = node2
    # # print l1.val
    # l2 = ListNode(0)
    # # node2 = ListNode(6)
    # # node3 = ListNode(4)
    # # node2.next = node3
    # # l2.next = node2
    #
    # for i in range(-1):
    #     print i
    #
    a = Solution()
    # result = a.addTwoNumbers(l1,l2)
    # while  result.next != None:
    #     print result.val
    #     result = result.next
    #     if result.next == None:
    #         print result.val
    print a.lengthOfLongestSubstring("tmmzuxmt")
    print a.findMedianSortedArrays([],[2,3])
    print a.longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc")
    print a.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
