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
