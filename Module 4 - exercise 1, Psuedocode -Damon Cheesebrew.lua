start
   set secretNumber to 71
   set guess to 0

   while guess is not equal to secretNumber
      output "Enter your guess (between 1 and 100):"
      input guess

      if guess is less than secretNumber then
         output "Too low!"
      else if guess is greater than secretNumber then
         output "Too high!"
      else
         output "Congratulations! You've guessed the correct number."
      endif
   endwhile
stop
