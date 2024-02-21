Attribute VB_Name = "Nested"
#If Win64 Then
Public Sub MySub(TempVar)
    MsgBox "64"
End Sub
#Else
Public Sub MySub(TempVar)
  #If VBA7 Then
    MsgBox "7"
  #Else
    MsgBox "6"
  #End If
    
  MsgBox "not 64"
End Sub
#End If
