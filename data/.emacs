;;;
;;; any .F77 or .f77 files open should use fortran mode
;;;
( setq auto-mode-alist ( append '(
		("\\.f77$". fortran-mode )
		("\\.F77$". fortran-mode )
) auto-mode-alist ) )
