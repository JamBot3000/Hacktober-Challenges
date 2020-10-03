# ----------------------------------------------------------------------------------------
#   Performs the caesar-cipher using x86 Linux assembly
#   Assemble it using GAS:
#     gcc caesar-cipher.s -o caesar
#    
#   Call it:
#     ./caesar <String to be encrypted> <Caesar rotation>
#     Only accepts uppercase Strings
# ----------------------------------------------------------------------------------------

    .global main

    .text
main:
    push    %r12
    push    %r13
    push    %r14
    # sub     $8, %rsp                # must align stack before calling

    cmp     $3, %rdi                # must have exactly two arguments, argc is in rdi
    jne     error_too_few_args

    mov     %rsi, %r12              # argv is in rsi

    mov     16(%r12), %rdi          # rotation-shift
    call    atoi
    mov     %rax, %r13              # rotation-shift as integer in r13

    xor     %rcx, %rcx              # clear rcx
    mov     8(%r12), %rcx           # put string into rcx


    xor     %rax, %rax              # clear eax, use as counter into the string
start_loop:
    xor     %rdx, %rdx              # clear rdx
    mov     (%rcx, %rax, 1), %dl    # load the byte at address rcx+rax in to the low byte of rdx, rcx is the address of the string, rax is the offset
    cmp     $0, %dl                 # check for the terminating NULL-byte
    je      end_loop                #   and escape the loop if encountered
    add     %r13, %rdx              # apply caesar-shift
    cmp     $90, %dl                # check if we overflowed at the end of the alphabet
    jle     no_overflow             #   if we did,
    sub     $26, %dl                #   Fix the overflow
no_overflow:
    mov     %dl, (%rcx, %rax, 1)    # Write the byte with the applied caesar-encryption back into memory
    inc     %eax                    # increment the counter
    jmp     start_loop              # loop

end_loop:
    mov     %rcx, %rdi              # Output the encrypted string
    call    puts                    
    jmp done

error_too_few_args:
    mov     $error_too_few_args_string, %edi    # Output warning for giving too few arguments
    call    puts
    jmp done

done:                               # Cleanup
    pop %r14
    pop %r13
    pop %r12
    ret

error_too_few_args_string:
    .ascii  "2 Arguments are needed!\n\0"
