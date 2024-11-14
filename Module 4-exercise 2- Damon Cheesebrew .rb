start
   set targetWord to "logic"
   set currentPage to open dictionary to a random page

   while currentPage does not contain targetWord
      if currentPage word is alphabetically before targetWord then
         flip forward
      else if currentPage word is alphabetically after targetWord then
         flip backward
      endif
      set currentPage to new page
   endwhile

   output "Found the word: " + targetWord
stop
