# Solve
objdumpでbinshとstr_headのアドレスを見ると差が0x10であることがわかる。  
The address of "input  " is 0x557ead01e010.  
と表示されたらそのアドレスに0x10加算したものがbinshのアドレスとなる。  
入力するとshellが立ち上がってflagが読み取れる。  
