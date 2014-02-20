;; .emacs

;;; uncomment this line to disable loading of "default.el" at startup
;; (setq inhibit-default-init t)

;; turn on font-lock mode
(when (fboundp 'global-font-lock-mode)
  (global-font-lock-mode t))

(add-to-list 'load-path "~/program_files/emacs-plugin/php-mode-1.5.0")
(require 'php-mode)
(add-hook 'php-mode-user-hook 'turn-on-font-lock)

(require 'package)
(add-to-list 'package-archives
	     '("melpa" . "http://melpa.milkbox.net/packages/") t)

(package-initialize)
(unless (package-installed-p 'scala-mode2)
    (package-refresh-contents) (package-install 'scala-mode2))



;; enable visual feedback on selections
;(setq transient-mark-mode t)

;; default to better frame titles
;(setq frame-title-format
;     (concat  " (%P) - emacs@" system-name))


;;display file path
;; display buffer name or absolute file path name in the frame title
;; Frame title bar formatting to show full path of file
     (setq-default mode-line-format
      (quote
       (#("-" 0 1
          (help-echo
           "mouse-1: select window, mouse-2: delete others ..."))
        mode-line-mule-info
        mode-line-modified
        mode-line-frame-identification
        ""
        mode-line-buffer-identification
	#("   %[(" 0 6
          (help-echo
           "mouse-1: select window, mouse-2: delete others ..."))
        (:eval (mode-line-mode-name))
        mode-line-process
        minor-mode-alist
        #("%n" 0 2 (help-echo "mouse-2: widen" local-map (keymap	.	..)))
        ")%] "
        (-3								.	"%P")
        ;;   "-%-"
	" "
        global-mode-string
	" "
        (:eval (substring
                (system-name) 0 (string-match "\\..+" (system-name))))
        ":"
        default-directory
        #(" " 0 1
          (help-echo
           "mouse-1: select window, mouse-2: delete others ..."))
        (line-number-mode " Line %l ")
;        global-mode-string
        
        )))



;set defual line spacding
(setq-default line-spacing 10)

;set scroll smoothy
(setq scroll-margin 3
     scroll-conservatively 10000)


(require 'ibuffer)
(global-set-key (kbd "C-x C-b") 'ibuffer)

;(require 'session)
;(add-hook 'after-init-hook 'session-initialize)

;(require 'lusty-explorer)

;open line number mode, and set the line number space to -3d,left align
(global-linum-mode t)
(setq linum-format "%-4d")

					;(setq tags-file-name "~/CVS/TAGS") ;set one TAG file
;(setq tags-table-list '("path1/TAGS" "path2/TAGS" "path3/TAGS"));;set several TAG files
;(setq tags-table-list '("~/CVS/TAGS"))
(global-linum-mode t)
;; TAGLIST-MODE ---------------------------------------------------------------
;(require 'taglist)
;(global-set-key "\C-xtg" 'taglist)


;load-path
;(add-to-list 'load-path "/home/yourname/.emacsLoadpath")

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 ;; '(custom-enabled-themes (quote (tsdh-dark)))
 '(display-time-mode t)
 '(inhibit-startup-screen t)
 '(send-mail-function (quote smtpmail-send-it))
 '(show-paren-mode t)
 '(tab-stop-list (quote (4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 100 104 108 112 116 120))) )

(setq visible-bell t);关闭出错时的蜂鸣提示声
;(mouse-avoidance-mode'animate);当鼠标箭头与光标相近时，使鼠标箭头自动移开
;(blink-cursor-mode nil);光标不闪烁
(setq-default cursor-type 'bar);光标显示为一竖线
;(tool-bar-mode -1);; 不显示emcas的工具栏
;(menu-bar-mode -1);; 不显示emcas的菜单栏,按ctrl+鼠标右键仍能调出该菜单
(setq x-select-enable-clipboard t);; 支持emacs和外部程序之间进行粘贴
(fset 'yes-or-no-p 'y-or-n-p);以 'y/n'字样代替原默认的'yes/no'字样
;(setq frame-title-format "%b----------****###@emacs");在最上方的标题栏显示当前buffer的名字
(setq make-backup-files nil);关闭自动备份功能
(setq auto-save-mode nil);关闭自动保存模式
(setq auto-save-default nil);不生成名为#filename# 的临时文件
(setq require-final-newline t);; 自动的在当前的buffer文件的最后加一个空行
(global-set-key "\r" 'align-newline-and-indent);;自动缩进<C-j>变为<Enter>
(setq echo-keystrokes 0.1);; 尽快显示按键序列提示
(global-font-lock-mode t);; 语法高亮
;; 用来显示当前光标在哪个函数
(require 'which-func)
(which-func-mode 1)
(setq which-func-unknown "unknown")
;; 用M-x执行某个命令的时候，在输入的同时给出可选的命令名提示
(icomplete-mode 1)
(define-key minibuffer-local-completion-map (kbd "SPC") 'minibuffer-complete-word)


;;;;;;;;;;;;;;;;;启动时最大化;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;(require 'maxframe)
;(add-hook 'window-setup-hook 'maximize-frame t)
;下载maxframe.el并放置在<load-path>中
;http://files.emacsblog.org/ryan/elisp/maxframe.el
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;web方式显示行号;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;(set-scroll-bar-mode 'right);滚动条在右侧
(set-scroll-bar-mode nil)   ; 不显示滚动条, even in x-window system (recommended)
;(require 'wb-line-number)
;(wb-line-number-toggle)
;下载wb-line-number.el并放置在<load-path>中
;http://homepage1.nifty.com/blankspace/emacs/elisp.html
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;cc-mode;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(add-to-list 'load-path "~/program_files/emacs-plugin/cc-mode-5.32.3")
(require 'cc-mode)

(add-to-list 'load-path "~/program_files/emacs-plugin/")
(require 'google-c-style)
(add-hook 'c-mode-common-hook 'google-make-newline-indent)
(add-hook 'c-mode-common-hook 'google-set-c-style)
(c-set-offset 'inline-open 0)
(c-set-offset 'friend '-)
(c-set-offset 'substatement-open 0)
(setq c-default-style "gnu"
      c-basic-offset 4)

(setq c-basic-offset 4)
(setq-default c-basic-offset 4)


;http://sourceforge.net/projects/cc-mode/?source=directory
;http://www.kklinux.com/html/linuxwangluojishu/linuxxitongguanliyuan/200902/28-3728.html
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;(add-to-list 'load-path "~/program_files/emacs-plugin/emacs-dirtree-master")
;(require 'tree-mode)
;(require 'windata)
;(require 'dirtree)
;(autoload 'dirtree "dirtree" "Add directory to tree view" t)
;(global-set-key [f2] 'dirtree-show)

;;auto-complete plugin
(add-to-list 'load-path "~/program_files/emacs-plugin/auto-complete-1-3-1")
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/program_files/emacs-plugin/auto-complete-1-3-1/ac-dict")
(ac-config-default)



;(global-set-key [M-left] 'windmove-left)          ; move to left windnow
;(global-set-key [M-right] 'windmove-right)        ; move to right window
;(global-set-key [M-up] 'windmove-up)              ; move to upper window
;(global-set-key [M-down] 'windmove-down)          ; move to downer window


;(global-set-key [?\C-=] 'make-symbolic-link)
;(global-set-key [?\M-\C-=] 'make-symbolic-link)
;(global-set-key [?\H-a] 'make-symbolic-link)
;(global-set-key [f7] 'make-symbolic-link)
;(global-set-key [C-mouse-1] 'make-symbolic-link)

;set the tarbar plugin
;http://wikemacs	.	org/wiki/Tabbar
(add-to-list 'load-path "~/program_files/emacs-plugin/")
(require 'tabbar)
(tabbar-mode t)
;(global-set-key (kbd "C-c C-n")  'tabbar-forward)
;(global-set-key (kbd "C-c C-p")  'tabbar-backward)

; define all tabs to be one of 3 possible groups: “Emacs Buffer”, “Dired”,
;“User Buffer”	.	

(defun tabbar-buffer-groups ()
    "Return the list of group names the current buffer belongs to		.	
This function is a custom function for tabbar-mode's tabbar-buffer-groups	.	
This function group all buffers into 3 groups:
Those Dired, those user buffer, and those emacs buffer				.	
Emacs buffer are those starting with “*”					.	"
      (list
          (cond
       ((string-equal "*" (substring (buffer-name) 0 1))
	     "Emacs Buffer"
	          )
	           ((eq major-mode 'dired-mode)
		         "Dired")
		       (t  "User Buffer"))))

(setq tabbar-buffer-groups-function 'tabbar-buffer-groups)

;(global-set-key [c-c-b] 'tabbar-backward)
;(global-set-key [c-c-f] 'tabbar-forward)




(global-set-key [(meta p)] 'tabbar-backward)
(global-set-key [(meta n)] 'tabbar-forward)
;; example tabbar coloring code...
  (set-face-attribute
     'tabbar-default nil
       :background "gray80"
	 :family "Bitstream Vera Sans Mono"
	 :foreground "gray30"
	 :height 0.75)
 (set-face-attribute
   'tabbar-unselected nil
   :inherit 'tabbar-default
   :background "gray85"
      :foreground "gray30"
      :box nil)

  (set-face-attribute
      'tabbar-selected nil
      :inherit 'tabbar-default
      :background "#f2f2f6"
      :foreground "#ff00ff"
      :box nil)

(set-face-attribute
      'tabbar-button nil
      :inherit 'tabbar-default
      :box '(
	     :line-width 1
	     :color "gray72"
	     :style released-button))

(set-face-attribute
      'tabbar-separator nil
         :height 1
	 :foreground "green")

;(setq tabbar-buffer-groups-function (lambda () (list "All buffers")))
(setq tabbar-cycling-scope nil)
(setq tabbar-home-button (quote (("[Home]") "[x]")))
(setq tabbar-separator (quote (" <|> ")))



;***********************************************************************
;(set-face-background 'default "gainsboro");背景设定
;颜色参考value：X界面菜单栏中[edit]->[text properties]->[Display colors]

;未完其他内容在本文的后续部分介绍
;session
;global(GNU GLOBAL source code tag system)
;##cedet(Collection of Emacs Development Environment Tools)
;##ecb(Emacs Code Browser)
;##doxymacs
;##compile

;##GDB

;##global(GNU GLOBAL source code tag system);;;;;;;;;;;;;;;;;;;;;
;to use global from Emacs, you need to load the `gtags.el' and execute gtags-mode function in it.
;you need to add it to load-path.for `gtags.el'file.

(setq load-path (cons "~/program_files/global-6.2.7/share/gtags/" load-path))
;(add-to-list 'load-path "~/program_files/global-6.2.7/share/gtags/");已经在之前的代码中load完了
;(require 'gtags)
(autoload 'gtags-mode "gtags" "" t);;start Emacs and execute gtags-mode function.
(setq c-mode-hook
            '(lambda ()
            (gtags-mode 1)));get into gtags-mode whenever you get into c-mode
(setq c++-mode-hook
      '(lambda ()
	 (gtags-mode 1)))
(setq java-mode-hook
      '(lambda ()
	 (gtags-mode 1)))
(setq asm-mode-hook
      '(lambda ()
	 (gtags-mode 1)))

;(add-hook 'c-mode-common-hook
;	            '(lambda()
;                   (gtags-mode 1)
;                (gtags-make-complete-list)))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(setenv "PATH" (concat (getenv "PATH") ":~/program_files/global-6.2.7/bin"))
(setq exec-path (append exec-path '("~/program_files/global-6.2.7/bin")))

(setenv "PATH" (concat (getenv "PATH") ":~/program_files/idutils-4-6/bin"))
(setq exec-path (append exec-path '("~/program_files/idutils-4-6/bin")))



;(set-face-background 'default "LightCyan3") ;;设置背景色为 浅青色3 
;(global-set-key (kbd "C-x C-b") 'ibuffer)
;(defalias 'ft 'gtags-find-tag)
;(global-set-key (kbd "C-c C-t") 'gtags-find-tag)
(global-set-key (kbd "C-]") 'gtags-find-tag)
(global-set-key (kbd "C-o") 'gtags-pop-stack)
(setq gtags-suggested-key-mapping t)
(setq gtags-prefix-key "\C-c")

;up directory short cut
(global-set-key (kbd "\C-c u") 'dired-up-directory)

;----------------------------------

(global-ede-mode 1)
;(require 'semantic/sb)
(semantic-mode 1)


;**********************idutils*********************************************
(add-to-list 'load-path "~/program_files/idutils-4-6/share/emacs/site-lisp")
(require 'idutils)

;http://www.ysbl.york.ac.uk/~emsley/software/stuff/uniquify.el
;show full path name
;(require 'uniquify)
;(setq uniquify-buffer-name-style 'reverse)

;(setq uniquify-buffer-name-style 'forward)
;(require 'uniquify)

;(setq display-time-day-and-date t
;      display-time-24hr-format t)
;(display-time)

;;http://www.cnblogs.com/ClarkChan/archive/2007/08/12/852616.html color to rgb map

(global-hl-line-mode t)
;(set-face-background 'hl-line "#f0fff0");ivory
(set-face-foreground 'hl-line "dark")
(set-face-background 'hl-line "blue")

;(set-face-foreground 'hl-line "#ff0000")
;(set-face-underline-p 'hl-line t)




;;specity the load path of color them files
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes")
;(load-theme 'zhangchao08-test-theme t)
;(load-theme 'tango t)
;(load-theme 'light-blue t)
;(load-theme 'wheatgrass t)
;(load-theme 'whiteboard t)
;(load-theme 'tango-dark t) ;five star
;(load-theme 'tsdh-light t)  ;this line disaperr dislike
;(load-theme 'dichromacy t)
;(load-theme 'misterioso t)
;(load-theme 'adwaita t)

;(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
; )

;;set coding system

(setq locale-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(set-selection-coding-system 'utf-8)


(setq default-buffer-coding-system 'utf-8)
(setq default-buffer-file-coding-system 'utf-8)

;(set-language-environment 'Chinese-GB)

(prefer-coding-system 'utf-8)
(prefer-coding-system 'chinese-iso-8bit)


(set-keyboard-coding-system 'utf-8)
(set-clipboard-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-buffer-file-coding-system 'utf-8)
(set-selection-coding-system 'utf-8)
(modify-coding-system-alist 'process "*" 'utf-8)
(setq default-process-coding-system
                  '(utf-8 . euc-cn))
(setq-default pathname-coding-system 'utf-8)



(require 'smart-compile)

(global-set-key (kbd "<f9>") 'smart-compile)
;(add-to-list 'smart-compile-alist
;	     '("~/emacs/.*" . "make -C ~/emacs"))

(require 'protobuf-mode) 
(require 'org-install)
(put 'dired-find-alternate-file 'disabled nil)

(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$"	.	org-mode))
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)


;(set-background-color "black") ;; 使用黑色背景
;(set-foreground-color "white") ;; 使用白色前景
;(set-face-foreground 'region "green")  ;; 区域前景颜色设为绿色
;(set-face-background 'region "blue") ;; 区域背景色设为蓝色

;(set-face-attribute 'default nil :height 1200)
(put 'narrow-to-region 'disabled nil)

;;Emacs out, choosing one of tis random modes to obfuscate the current buffer, which can be used as a screensaver
(require 'zone)
(zone-when-idle 1200)

(global-semantic-idle-summary-mode t)
;(global-semantic-idle-completions-mode t)

