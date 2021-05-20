# 解法
__malloc_hookをFSAによってone_gadgetに書き換える。  
printfで長い文字列を出力するとmallocが呼ばれるので、  
printf("%65536c");などで長い文字列を出力する。  
