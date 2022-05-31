vim.cmd([[
let g:ripple_repls = {}
let g:ripple_repls["python"] = {
    \ "command": "ptipython",
    \ "pre": "\<esc>[200~",
    \ "post": "\<esc>[201~",
    \ "addcr": 1,
    \ "filter": 0,
    \ }
]])

