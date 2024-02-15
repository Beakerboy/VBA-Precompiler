Attribute VB_Name = "Boolean"
#if True And True Then
    foo = 2
#endif

#if True Or False Then
    foo = 3
#endif

#if True Xor False Then
    foo = 4
#endif

#if False Eqv False Then
    foo = 2
#endif

#if True Imp True Then
    foo = 4
#endif
