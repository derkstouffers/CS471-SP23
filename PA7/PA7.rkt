; Deric Shaffer
; CS471 - PA7
; Due Date - April 18th, 2023

#lang racket/base

; power_four
(define (power_four n)
  (cond
    ((zero? (modulo n 4)))
    (else #f)
  )
)

; insert_at
(define (insert_at pos n list1)
  (cond
    ((eq? pos 0) (cons n list1))
    ((null? list1) list1)
    (else (cons (car list1) (insert_at (- pos 1) n (cdr list1))))
  )
)

; helper function for palindrome_p
(define (last_element list1)
  (cond
    ((= (length list1) 1) (car list1))
    (else (last_element (cdr list1)))
  )
)

; helper function for palindrome_p
(define (rem_last list1)
  (cond
    ((= (length list1) 1) (remove (car list1) list1))
    (else (cons (car list1) (rem_last (cdr list1))))
  )
)

; palindrome_p   
(define (palindrome_p list1)
  (cond
    ((< (length list1) 2) 1)
    ((equal? (car list1) (last_element list1)) (palindrome_p (rem_last (cdr list1))))
    (else 0)
  )
)

; if_prime 
(define (if_prime n i)
  (cond
    ((<= n 2) (eq? n 2))
    ((zero? (modulo n i)) 1) ; 1 = not prime
    ((> (* i i) n) 0) ; 0 = prime 
    (else (if_prime n (+ i 1)))
  )
)

; power_four test cases
(power_four 16)
(power_four 99)

; insert_at test cases
(insert_at 0 5 '(1 2 3 4))
(insert_at 1 5 '(1 2 3 4))
(insert_at 2 5 '(1 2 3 4))
(insert_at 3 5 '(1 2 3 4))
(insert_at 4 5 '(1 2 3 4))

; palindrome_p test cases
(palindrome_p '(1 2 3 2 1))
(palindrome_p '(1 2 1 2 1))
(palindrome_p '(1 2 3 4))

; if_prime test cases
(if_prime 19 2)
(if_prime 25 2)