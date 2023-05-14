! Deric Shaffer
! CS471 - PA3
! Due Date: March 5th, 2023

program gauss_f
    implicit none

    ! variables
    integer :: i, j
    integer, parameter :: size = 2000
    real :: strt, stp

    real :: mat(size, size + 1)

    real :: b(size)

    real :: x

    ! populate matrices with random numbers
    call random_number(mat)
    call random_number(b)


    call cpu_time(strt)

    do i = 1, size
        do j = i + 1, size
            mat(j, :) = mat(j, :) - mat(i, :) * mat(j, i) / mat(i, i)
        end do
    end do

    do i = size, 1, -1
        x = mat(i, size + 1)
        do j = i + 1, size
            x = x - mat(i, j) * b(j)
        end do
        b(i) = x / mat(i, i)
    end do

    call cpu_time(stp)

    print *, stp - strt

end program gauss_f