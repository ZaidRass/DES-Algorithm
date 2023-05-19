from textwrap import wrap


def Get_S_box(number): #This function takes the number of the S-box and returns the corresponding S-box 

  #Every S-box is represented as a list of lists 
  #Every list in each list of lists represents a row in the corresponding S-box
  s1 =[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
  s2= [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
  s3= [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
  s4= [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
  s5= [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
  s6= [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
  s7= [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
  s8= [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
  switcher = {
      0 : s1,
      1 : s2,
      2 : s3,
      3 : s4,
      4 : s5,
      5 : s6,
      6 : s7,
      7 : s8
  }
  return(switcher.get(number))

#This function takes a string of 6 bits and the desired s_box as inputs and returns a string of 4 bits after substitution
def Substitution(value , s_box): 
  row = int(value[0] + value[5] , 2)
  column = int(value[1]+value[2]+value[3]+ value[4] , 2)
  value = bin(s_box[row][column])[2:]
  while(len(value) < 4):
    value = '0' + value
  return value

#Function to do the initial permutaion
def Initial_permutation(message,InitualPermutationList):
   Initial_permutationText = ""
   for i in InitualPermutationList:
    for j in i:
      Initial_permutationText += message[j-1]
   return Initial_permutationText

#Function to do the Key extension
def Right_Key_Extension(Right_Value,Extension_List):
  funct_outcome=""
  for i in Extension_List:
    for j in i:
      funct_outcome += Right_Value[j-1]
  return funct_outcome

#Second permutation
def Secondary_Permutation(Value,P_Function_List):
    Second_Permutation=""
    for i in P_Function_List:
      for j in i:
        Second_Permutation += Value[j-1]
    return Second_Permutation

#Final permutation
def Final_Permutation(Value, Final_Permutation_List):
  Final_Permutation_Text=""
  for i in Final_Permutation_List:
    for j in i:
      Final_Permutation_Text+=Value[j-1]
  return Final_Permutation_Text

#XOR function
def XOR(String_1,String_2):
  res=""
  for i in range(len(String_2)):
    if String_1[i] != String_2[i]:
      res+="1"
    else:
      res+="0"
  return res

def Encrypt(message , keys):
  #Every list in initial_permutation list of lists represents a row in the initial permutation table
  initial_permutation= [[58,50,42,34,26,18,10,2],[60,52,44,36,28,20,12,4],[62,54,46,38,30,22,14,6],[64,56,48,40,32,24,16,8],[57,49,41,33,25,17,9,1],[59,51,43,35,27,19,11,3],[61,53,54,37,29,21,13,5],[63,55,47,39,31,23,15,7]]

  #Every list in e_bit_selection list of lists represents a row in the e_bit_selection_table 
  e_bit_Selection = [[32,1,2,3,4,5],[4,5,6,7,8,9],[8,9,10,11,12,13],[12,13,14,15,16,17],[16,17,18,19,20,21],[20,21,22,23,24,25],[24,25,26,27,28,29],[28,29,30,31,32,1]]


  #Every list in p_function list of lists represents a row in p_function table 
  p_function = [[16,7,20,21],[29,12,28,17],[1,15,23,26],[5,18,31,10],[2,8,24,14],[32,27,3,9],[19,13,30,6],[22,11,4,25]]

  #Every list in final_permutation list of lists represents a row in final_premutation table 
  final_permutation = [[40,8,48,16,56,24,64,32],[39,7,47,15,55,23,63,31],[38,6,46,14,54,22,62,30],[37,5,45,13,53,21,61,29],[36,4,44,12,52,20,60,28],[35,3,43,11,51,19,59,27],[34,2,42,10,50,18,58,26],[33,1,41,9,49,17,57,25]]

  #Write your implementation here
  #To do the initial premutation
  Initial_permutationText=Initial_permutation(message,initial_permutation)
  #To split the Initial permutation and put it in L0 and R0
  Left = Initial_permutationText[:32]
  Right = Initial_permutationText[32:]
  #16 rounds
  Rounds = 0
  while Rounds<16:  
    Expansion_of_Right_Key = Right_Key_Extension(Right,e_bit_Selection)
    # extends the right value to 48-bits to be match the key
    #XOR the outcome from the extension with our key
    XOR_With_Key= str(XOR(Expansion_of_Right_Key,keys[Rounds]))
    #splits the XOR key into a List and each list has a size of 6 bits 
    XOR_With_Key_List = wrap(XOR_With_Key,6)  
    Sbox=0
    Shrinked_Right_Value=""
    # I subtracted 1 from the SBoX values in the method:Get_S_Box 
    while Sbox<8:
      #Get the sbox from the function
      GetSbox= Get_S_box(Sbox)
      
      #Shrink the right half to 32 bits
      Shrinked_Right_Value+=Substitution(XOR_With_Key_List[Sbox] , GetSbox)
      #Counter to loop on the S-Box
      Sbox+=1

    Rounds+=1
    #To perform the Second permutation
    Second_Permutation= Secondary_Permutation(Shrinked_Right_Value,p_function)
    temp =Right
    #Xor the left half with the result of the second permutation
    Right= XOR(Left,Second_Permutation)
    Left=temp
  #Swap the left with the right
  Temp= Right+Left
  #perform the final permutation
  Final_Outcome = Final_Permutation(Temp,final_permutation)
  return Final_Outcome

  
   

 

message = "0000000100100011010001010110011110001001101010111100110111101111"

keys = ["000110110000001011101111111111000111000001110010",
        "011110011010111011011001110110111100100111100101",
        "010101011111110010001010010000101100111110011001",
        "011100101010110111010110110110110011010100011101",
        "011111001110110000000111111010110101001110101000",
        "011000111010010100111110010100000111101100101111",
        "111011001000010010110111111101100001100010111100",
        "111101111000101000111010110000010011101111111011",
        "111000001101101111101011111011011110011110000001",
        "101100011111001101000111101110100100011001001111",
        "001000010101111111010011110111101101001110000110",
        "011101010111000111110101100101000110011111101001",
        "100101111100010111010001111110101011101001000001",
        "010111110100001110110111111100101110011100111010",
        "101111111001000110001101001111010011111100001010",
        "110010110011110110001011000011100001011111110101"]
  
print(Encrypt(message, keys)) #you should get 1000010111101000000100110101010000001111000010101011010000000101