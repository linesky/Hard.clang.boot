
	.text
	.section	.rodata
.LC0:
	.string	"\033[43;37mhello world....\n"
	.text
	.align	2
	.globl	main
	.type	main, @function
main:
	link.w %fp,#-4
	move.l #.LC0,-4(%fp)
	move.l -4(%fp),-(%sp)
	jsr printf
	addq.l #4,%sp
	clr.l %d0
	unlk %fp
	rts

