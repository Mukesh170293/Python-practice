def versionCompare(v1, v2):
	arr1 = v1.split(".")
	arr2 = v2.split(".")
	n = len(arr1)
	m = len(arr2)
	arr1 = [int(i) for i in arr1]
	arr2 = [int(i) for i in arr2]
	if n>m:
	    for i in range(m, n):
	        arr2.append(0)
	elif m>n:
	    for i in range(n, m):
	        arr1.append(0)
	for i in range(len(arr1)):
	    if arr1[i]>arr2[i]:
	        return 1
	    elif arr2[i]>arr1[i]:
	        return -1
	return 0
version1 = "1.0.3"
version2 = "1.0.7"
ans = versionCompare(version1, version2)
print(ans)
