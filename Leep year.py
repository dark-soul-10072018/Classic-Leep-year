#dArK sOuL

print ("""
""")
print("¿ dArK sOuL ?".center(50))
print("""
""")

# input

a =  int (input ("Enter the year: "))

al1 = str (a)
al2 = len (al1)
if al2 != 4:
   print ("""
            Invalid year
""")
elif al2 == 4: 

# type determine

   a1 = float (a/100)
   x = (a1 - int (a1))
   if x != 0:

# Formula for 4
      b = (a/4)
      ba = abs ((round (b,0) -b))

# If function for 4

      if ba == 0:
          print ("")
          print ("This is a leep year")
      elif ba != 0:
         print ("")
         print ("This is not a leep year")
  
# Formula for 400
   elif x == 0:
      b = (a/400)
      ba = abs ((round (b,0) -b))

# If function for 400

      if ba == 0:
         print ("")
         print ("This is a leep year")
      elif ba != 0:
         print ("")
         print ("This is not a leep year")

#dArK sOuL

print ("""
""")
print("¿ dArK sOuL ?".center(50))
print("""
""")