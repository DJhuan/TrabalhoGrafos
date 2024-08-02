rodar_direita :: Int -> [a] -> [a]
rodar_direita 0 lista = lista
rodar_direita n lista = rodar_direita (n - 1) (ultimoElemento lista : primeirosElementos lista)

ultimoElemento :: [a] -> a
ultimoElemento [x] = x
ultimoElemento (_:r) = ultimoElemento r

primeirosElementos :: [a] -> [a]
primeirosElementos [x] = []
primeirosElementos (c:r) = c : primeirosElementos r
