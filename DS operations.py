n=int(input("Enter size:"))
l=[]
for i in range(1,n+1):
    x=int(input("Enter the element to insert:"))
    l.append(x)
print(l)
print("The Operations are:")
print("1.Insert")
print("2.Delete")
print("3.Search")
print("4.Sort")
print("5.Exit")
while(True):
    q=int(input("Enter your choice:"))
    match(q):
          case 1:
              s=int(input("Enter the element you want to insert:"))
              l.append(s)
              print("The updated array is-",l)
          case 2:
              e=int(input("Enter the element you want to delete:"))
              l.remove(e)
              print("The updated array is-",l)
          case 3:
              d=int(input("Enter the element you want to search:"))
              if d in l:
                  print("Element found")
              else:
                  print("Element not found")
          case 4:
              l.sort()
              print("The sorted array is-",l)
          case 5:
              break
        
        
      
