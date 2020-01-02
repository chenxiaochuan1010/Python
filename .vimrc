" .vimrc created by Chen Xiaochuan, Dec. 2019
" version: 0.1


set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

if filereadable(expand("~/.vimrc.bundles"))
  source ~/.vimrc.bundles
endif


" 将ESC键映射为两次j键                                      
inoremap jj <Esc>

" 将leader键设置为空格键
let mapleader = "\<space>"


" 窗口移动键位映射
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" 主题颜色
colorscheme snazzy
let g:SnazzyTransparent=1

" 状态栏
let g:lightline = {
\ 'colorscheme': 'snazzy',
\ }

" 目录文件导航NERD-Tree
" \nt 打开nerdree窗口，在侧栏显示
nmap <Leader>nt :NERDTree<CR>
let NERDTreeWinPos="right"
"close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"NERDTree auto start when opening a directory
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | exe 'cd '.argv()[0] | endif
let NERDTreeQuitOnOpen=1
""不显示隐藏文件
let g:NERDTreeHidden=0

" 运行文件
"map <F5> :w<cr>:r!python3 %<cr>
"按F5运行python"
map <F5> :call RunPython()<CR>
func! RunPython()
    exec "W"
    if &filetype == 'python'
        exec "!time python3.6 %"
    endif
endfunc

"语法高亮
filetype off
filetype plugin indent on
syntax on
"let python_highlight_all=1

" 设置行号以及长度
set number "show line numbers
set colorcolumn=80
set cursorline

" 逐步查找开启
set incsearch
" 设置默认进行大小写不敏感查找
set ignorecase
" 如果有一个大写字母，则切换到大小写敏感查找
set smartcase
" 当光标一段时间保持不动了，就禁用高亮
autocmd cursorhold * set nohlsearch
" 当输入查找命令时，再启用高亮
noremap n :set hlsearch<cr>n
noremap N :set hlsearch<cr>N
noremap / :set hlsearch<cr>/
noremap ? :set hlsearch<cr>?
noremap * *:set hlsearch<cr>

" 历史记录条数
set history=700
set undolevels=700

" 禁止备份与SWAP
set nobackup
set nowritebackup
set noswapfile

" 空格替代TABs
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround

"文件编码
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
set fileencoding=utf-8

" 缩进
set autoindent

" 修正vim退格键怪异行为
set backspace=eol,start,indent

" 状态栏双行
set laststatus=2


" MRU
nmap <Leader>mr :MRU<CR>

" jedi提示窗移到状态栏下方
"let jedi#show_call_signatures=2
" Supertab+jedi代码补全
"let g:SuperTabDefaultCompletionType = "context"
"let g:jedi#popup_on_dot = 0

" Markdown preview键位映射
nmap <silent> <F8> <Plug>MarkdownPreview        " for normal mode
imap <silent> <F8> <Plug>MarkdownPreview        " for insert mode
nmap <silent> <F9> <Plug>StopMarkdownPreview    " for normal mode
imap <silent> <F9> <Plug>StopMarkdownPreview    " for insert mode

" Autoformat配置
nnoremap <F6> :Autoformat<CR>
let g:autoformat_autoindent = 0
let g:autoformat_retab = 0
let g:autoformat_remove_trailing_spaces = 0


set linebreak


